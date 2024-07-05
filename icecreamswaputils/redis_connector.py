import json
import os
import socket
from enum import Enum
from typing import Optional

import platform
import numpy as np
import pandas as pd
import pyarrow.feather as feather
import redis
import io

from hexbytes import HexBytes
from web3.datastructures import AttributeDict

from .safe_thread import SafeThread
from .callback_registry import CallbackRegistry


class Serialization(Enum):
    JSON = 1
    FEATHER = 2


class RedisConnector(CallbackRegistry):
    SERIALIZATION_BY_PREFIX: dict[str, Serialization] = {
        "blocks": Serialization.JSON,
        "pools:uniswap-v2": Serialization.FEATHER,
        "pools:uniswap-v3": Serialization.JSON,
        "block_id:pools:uniswap-v2": Serialization.JSON,
        "block_id:pools:uniswap-v3": Serialization.JSON,
        "block_id:fees": Serialization.JSON,
        "fees": Serialization.FEATHER,
        "non_flashswap_pools": Serialization.JSON,
        "working:uniswap-v3": Serialization.JSON,
        "block_id:working:uniswap-v3": Serialization.JSON,
    }

    def __init__(
            self,
            redis_host: str = 'localhost',
            redis_port: int = 6379,
            redis_db: int = 0,
    ):
        super().__init__()
        if platform.system() == 'Darwin':
            keep_alive_options = {
                socket.TCP_KEEPALIVE: 60,
                socket.TCP_KEEPINTVL: 5,
                socket.TCP_KEEPCNT: 3,
            }
        else:
            keep_alive_options = {
                socket.TCP_KEEPIDLE: 60,
                socket.TCP_KEEPINTVL: 5,
                socket.TCP_KEEPCNT: 3,
            }
        self.r = redis.Redis(
            host=redis_host,
            port=redis_port,
            db=redis_db,
            socket_keepalive=True,
            socket_keepalive_options=keep_alive_options
        )
        self.r.ping()

    def __setitem__(self, redis_key: str, data):
        if isinstance(data, AttributeDict):
            data = data.__dict__

        if isinstance(redis_key, str):
            data_serialized = self.serialize_data(redis_key, data)
            self.r.set(redis_key, data_serialized)
        else:
            # redis hash
            key, hkey = redis_key
            if isinstance(hkey, str):
                data_serialized = json.dumps(data)
                self.r.hset(key, hkey, data_serialized)
                updated_hashes = [hkey]
            elif isinstance(hkey, slice):
                mapping = {key: json.dumps(value) for key, value in data.items()}
                # overwrite mapping in redis
                with self.r.pipeline() as pipe:
                    pipe.delete(key)
                    if len(mapping) != 0:
                        pipe.hset(key, mapping=mapping)
                    pipe.execute()
                updated_hashes = list(mapping.keys())
            else:
                assert len(hkey) == len(data)

                updates: dict = {}
                deletes: list = []
                for redis_hash, value in zip(hkey, data):
                    if value is None:
                        deletes.append(redis_hash)
                    else:
                        updates[redis_hash] = json.dumps(value)

                if len(updates) > 0:
                    self.r.hset(key, mapping=updates)
                if len(deletes) > 0:
                    # remove keys from mapping that have a None value
                    self.r.hdel(key, *deletes)
                updated_hashes = list(hkey)

            # create our own kind of keyspace notifications for individual hash keys
            self.publish(f"hash_updates:{key}", updated_hashes)

    def __getitem__(self, redis_key: str | tuple[str, str | list[str]]):
        if isinstance(redis_key, str):
            data_serialized = self.r.get(redis_key)
            return self.deserialize_data(redis_key, data_serialized)
        else:
            # redis hash
            key, hkey = redis_key
            if isinstance(hkey, str):
                return json.loads(self.r.hget(key, hkey))
            elif isinstance(hkey, slice):
                assert hkey.start is None and hkey.step is None and hkey.stop is None, "only : allowed"
                data_raw = self.r.hgetall(key)
                return {key_encoded.decode(): json.loads(value_serialized) for key_encoded, value_serialized in data_raw.items()}
            else:
                values_serialized = self.r.hmget(key, hkey)
                return {key: json.loads(value_serialized) for key, value_serialized in zip(hkey, values_serialized)}

    def publish(self, redis_key: str, data):
        data_serialized = RedisConnector.to_json(data)
        self.r.publish(channel=redis_key, message=data_serialized)

    def subscribe(self, redis_key: str, decode: bool = False, channel: Optional[str] = None, thread_name: Optional[str] = None) -> SafeThread:
        thread = SafeThread(target=self._subscribe_thread, name=thread_name, kwargs=dict(
            redis_key=redis_key,
            decode=decode,
            channel=channel
        ))
        thread.start()
        return thread

    def _subscribe_thread(self, redis_key: str, decode: bool = False, channel: Optional[str] = None):
        pubsub = self.r.pubsub(ignore_subscribe_messages=True)

        if "*" in redis_key:
            pubsub.psubscribe(redis_key)
        else:
            pubsub.subscribe(redis_key)

        for message in pubsub.listen():
            if decode:
                data = self.deserialize_data(message["channel"].decode(), message["data"])
                self._on_new_data(data, channel=channel)
            else:
                self._on_new_data(message, channel=channel)
        raise Exception("should never return")

    def subscribe_hash(self, redis_key: str, channel: Optional[str] = None) -> SafeThread:
        thread = SafeThread(
            target=self._subscribe_hash_thread,
            kwargs=dict(
                redis_key=redis_key,
                channel=channel
            ),
            name=f"redis_subscriber_{redis_key}"
        )
        thread.start()
        return thread

    def _subscribe_hash_thread(self, redis_key: str, channel: Optional[str] = None):
        data_raw = self.r.hgetall(redis_key)
        data = {key_encoded.decode(): json.loads(value_serialized) for key_encoded, value_serialized in data_raw.items()}
        del data_raw

        self._on_new_data(data, list(data.keys()), channel=channel)

        pubsub = self.r.pubsub(ignore_subscribe_messages=True)

        pubsub.subscribe(f"hash_updates:{redis_key}")

        for message in pubsub.listen():
            changed_keys: list[str] = json.loads(message["data"])
            if len(changed_keys) == 0:
                continue
            changed_values_serialized = self.r.hmget(redis_key, changed_keys)
            for key, value_serialized in zip(changed_keys, changed_values_serialized):
                if value_serialized is None:
                    del data[key]
                else:
                    data[key] = json.loads(value_serialized)
            self._on_new_data(data, changed_keys, channel=channel)
        raise Exception("should never return")

    def enable_keyspace_notifications(self):
        if os.getenv("REDIS_NO_KEYSPACE_NOTIFICATIONS_OVERWRITE") is not None:
            return
        self.r.config_set('notify-keyspace-events', 'K$h')

    @staticmethod
    def get_serialization(redis_key: str) -> Serialization:
        prefix = ":".join(redis_key.split(":")[:-1])
        serialization = RedisConnector.SERIALIZATION_BY_PREFIX[prefix]
        return serialization

    @staticmethod
    def serialize_data(redis_key, data) -> str:
        serialization = RedisConnector.get_serialization(redis_key=redis_key)

        if serialization == Serialization.FEATHER:
            data_serialized = RedisConnector.to_feather(data)
        elif serialization == Serialization.JSON:
            data_serialized = RedisConnector.to_json(data)
        else:
            raise AttributeError(f"unhandled serialization type: {serialization.name}")

        return data_serialized

    @staticmethod
    def deserialize_data(redis_key: str, data_serialized: bytes):
        serialization = RedisConnector.get_serialization(redis_key=redis_key)

        if serialization == Serialization.FEATHER:
            data = RedisConnector.from_feather(data_serialized)
        elif serialization == Serialization.JSON:
            data = RedisConnector.from_json(data_serialized)
        else:
            raise AttributeError(f"unhandled serialization type: {serialization.name}")

        return data

    @staticmethod
    def to_feather(data: pd.DataFrame) -> bytes:
        # Serialize the data to a Feather buffer
        buffer = io.BytesIO()
        feather.write_feather(data, buffer)
        buffer.seek(0)
        return buffer.getvalue()

    @staticmethod
    def from_feather(data_serialized: bytes) -> pd.DataFrame:
        buffer = io.BytesIO(data_serialized)
        df = feather.read_feather(buffer)
        return df

    @staticmethod
    def to_json(data) -> str:
        try:
            return json.dumps(data, default=RedisConnector.json_default)
        except Exception as e:
            raise e

    @staticmethod
    def from_json(data_serialized: bytes):
        data = json.loads(data_serialized)
        return data

    @staticmethod
    def json_default(data):
        if isinstance(data, HexBytes):
            return data.hex()
        if isinstance(data, AttributeDict):
            return data.__dict__
        if isinstance(data, np.ndarray):
            return data.tolist()
        return data

import json
import os
import socket
from enum import Enum
from typing import Union, Optional

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
        "tx:pending": Serialization.JSON,
    }

    def __init__(
            self,
            redis_host: str = 'localhost',
            redis_port: int = 6379,
            redis_db: int = 0,
    ):
        super().__init__()
        self.r = redis.Redis(
            host=redis_host,
            port=redis_port,
            db=redis_db,
            socket_keepalive=True,
            socket_keepalive_options={
                socket.TCP_KEEPALIVE: 60,
                socket.TCP_KEEPINTVL: 5,
                socket.TCP_KEEPCNT: 3,
            }
        )
        self.r.ping()

    def __setitem__(self, redis_key: str, data):
        if isinstance(data, AttributeDict):
            data = data.__dict__

        data_serialized = self.serialize_data(redis_key, data)

        self.r.set(redis_key, data_serialized)

    def __getitem__(self, redis_key: str):
        data_serialized = self.r.get(redis_key)

        return self.deserialize_data(redis_key, data_serialized)

    def update_hash(self, redis_key: str, values: dict, upsert: bool = True):
        values_partly_serialized: dict[str, Union[str, int, float, bytes]] = {}
        for key, value in values.items():
            if isinstance(value, str) or isinstance(value, int) or isinstance(value, float) or isinstance(value, bytes):
                value_serialized = value
            else:
                value_serialized = json.dumps(value)
            values_partly_serialized[key] = value_serialized

        if upsert:
            # upsert mapping
            updates = {key: value for key, value in values_partly_serialized.items() if values[key] is not None}
            deletes = [key for key, value in values_partly_serialized.items() if values[key] is None]

            if len(updates) > 0:
                self.r.hset(redis_key, mapping=updates)
            if len(deletes) > 0:
                # remove keys from mapping that have a None value
                self.r.hdel(redis_key, *deletes)
        else:
            # overwrite mapping in redis
            with self.r.pipeline() as pipe:
                pipe.delete(redis_key)
                pipe.hset(redis_key, mapping=values_partly_serialized)
                pipe.execute()

    def publish(self, redis_key: str, data):
        data_serialized = self.serialize_data(redis_key, data)
        self.r.publish(channel=redis_key, message=data_serialized)

    def subscribe(self, redis_key: str, decode: bool = False, channel: Optional[str] = None) -> SafeThread:
        thread = SafeThread(target=self._subscribe_thread, kwargs=dict(
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

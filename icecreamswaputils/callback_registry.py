from random import randint
from time import time
from typing import Optional


class CallbackRegistry:

    def __init__(
            self,
            callback_max_s=0.5,
    ):
        self.callback_max_s = callback_max_s

        self.callbacks: dict[Optional[str], dict[int, callable]] = dict()

    def register_callback(self, callback: callable, channel: Optional[str] = None) -> int:
        callback_id = randint(0, 2**32)
        if channel not in self.callbacks:
            self.callbacks[channel] = {}
        self.callbacks[channel][callback_id] = callback
        return callback_id

    def unregister_callback(self, callback_id):
        for channel in self.callbacks.keys():
            if callback_id in self.callbacks[channel]:
                self.callbacks[channel].pop(callback_id)
                break
        else:
            raise ValueError(f"callback_id {callback_id} not registered in callbacks")

    def _on_new_data(self, *args, channel: Optional[str] = None, **kwargs):
        start_time = time()

        # list parsing is to copy the values so there is no exception when the dict changes
        for callback in list(self.callbacks.get(channel, {}).values()):
            callback(*args, **kwargs)

        end_time = time()
        if end_time - start_time > self.callback_max_s:
            print(f"callback took to long, took {end_time - start_time}s, limit {self.callback_max_s}s")

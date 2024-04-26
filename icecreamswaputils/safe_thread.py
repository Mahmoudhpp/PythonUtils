from threading import Thread
import logging
from typing import Any


class SafeThread(Thread):
    def __init__(self, daemon=True, target=None, log_exception=False, **kwargs):
        self.exception = None
        self.result = None
        self.joined = False

        self.original_target = target if target is not None else self.run_safe
        self.log_exception = log_exception

        super().__init__(target=self._target_wrapper, daemon=daemon, **kwargs)

    def _target_wrapper(self, *args, **kwargs):
        try:
            self.result = self.original_target(*args, **kwargs)
        except Exception as e:
            self.exception = e
            if self.log_exception:
                logging.exception("Exception in SafeThread")

    def run_safe(self):
        raise NotImplementedError("either provide target ot overwrite run_save for SafeThread")

    def run(self):
        # should never get overwritten, use run_save!
        super().run()

    def join(self, *args, **kwargs) -> Any:
        super().join(*args, **kwargs)
        self.joined = True
        if self.exception is not None:
            self.raise_exception()
        return self.result

    def raise_exception(self):
        if self.exception is not None:
            raise self.exception
        raise ValueError("Thread has no Exception to raise")

    def __del__(self):
        if not self.joined and self.exception is not None:
            logging.exception("unhandled Exception in SafeThread", exc_info=self.exception)

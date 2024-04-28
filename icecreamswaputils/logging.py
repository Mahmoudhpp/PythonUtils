import logging
import sys
from multiprocessing import current_process

def get_logger(name, level=logging.INFO):
    logger = logging.Logger(name=name, level=level)
    if current_process().name == "MainProcess":
        logging_formatter = logging.Formatter('[%(asctime)s.%(msecs)03d %(threadName)s %(name)s %(levelname)s] %(message)s', "%H:%M:%S")
    else:
        logging_formatter = logging.Formatter('[%(asctime)s.%(msecs)03d %(processName)s %(threadName)s %(name)s %(levelname)s] %(message)s', "%H:%M:%S")
    stdout_handler = logging.StreamHandler(sys.stdout)
    stderror_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setLevel(level)
    stderror_handler.setLevel(logging.WARNING + 1)
    stdout_handler.setFormatter(logging_formatter)
    stderror_handler.setFormatter(logging_formatter)
    stdout_handler.addFilter(lambda record: record.levelno <= logging.WARNING)
    logger.addHandler(stdout_handler)
    logger.addHandler(stderror_handler)
    return logger
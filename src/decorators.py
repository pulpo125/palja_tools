import time
from functools import wraps

from src.utils import logger


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed_time = end - start
        logger.info(f"Execution time of {func.__name__}(): {elapsed_time:.4f} seconds")
        return result

    return wrapper

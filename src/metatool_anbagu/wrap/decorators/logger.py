from functools import wraps
import logging

def logged(func):
    logger = logging.getLogger(func.__module__)
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"Calling {func.__qualname__}")
        result = func(*args, **kwargs)
        logger.debug(f"Finished {func.__qualname__}")
        return result

    return wrapper
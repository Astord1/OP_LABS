import logging
import functools
import time
import inspect
import json
from datetime import datetime
from typing import Callable, Optional, Literal

LogLevel = Literal["DEBUG", "INFO", "ERROR"]

def setup_logger(name: str, level: str = "INFO", to_file: Optional[str] = None, json_format: bool = False):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # Avoid duplicate handlers

    logger.setLevel(getattr(logging, level.upper()))
    formatter = JsonFormatter() if json_format else logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    handler = logging.FileHandler(to_file) if to_file else logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "name": record.name
        }
        return json.dumps(log_entry)

def log(level: LogLevel = "INFO", to_file: Optional[str] = None, json_format: bool = False):
    logger = setup_logger("decorated_logger", level, to_file, json_format)

    def decorator(func: Callable):
        is_async = inspect.iscoroutinefunction(func)

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            start = time.time()
            try:
                logger.debug(f"Calling {func.__name__} with {args=} {kwargs=}")
                result = await func(*args, **kwargs)
                duration = time.time() - start
                if level in ["INFO", "DEBUG"]:
                    logger.info(f"{func.__name__} returned {result!r} in {duration:.4f}s")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} raised {e!r}")
                raise

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            start = time.time()
            try:
                logger.debug(f"Calling {func.__name__} with {args=} {kwargs=}")
                result = func(*args, **kwargs)
                duration = time.time() - start
                if level in ["INFO", "DEBUG"]:
                    logger.info(f"{func.__name__} returned {result!r} in {duration:.4f}s")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} raised {e!r}")
                raise

        return async_wrapper if is_async else sync_wrapper

    return decorator

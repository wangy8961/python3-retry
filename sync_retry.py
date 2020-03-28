from functools import wraps
import time

from logger import logger


def retry(tries=3, interval=0.3):
    """装饰器: 任何函数被调用时，如果抛出异常，允许重试"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            count = 0
            while True:
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    count += 1
                    if count > tries:  # 重试次数用完后，还是有异常时，只能往上抛出了
                        raise e
                    else:
                        logger.warning('Failed to call func {0}({4}, {5}), retrying in {1} seconds(total: {2}, retry: {3}). Exception: {6}'.format(func.__name__, interval, tries, count, args, kwargs, e))
                        time.sleep(interval)
                else:
                    return result
        return wrapper
    return decorator

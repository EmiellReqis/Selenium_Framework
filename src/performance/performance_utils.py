from functools import wraps
import time
import logging


def measure_performance(action_name: str):
    """
    Decorator to measure the performance of a function.

    :param action_name: Name of the action being measured
    :return: Wrapped function with performance measurement
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self = args[0]
            logger = self.logger
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time

            threshold = self.performance_thresholds.get(action_name, float('inf'))
            if duration > threshold:
                log_level = logging.WARNING
                tag = "PERFORMANCE WARNING"
            else:
                log_level = logging.getLevelName("PERFORMANCE")
                tag = "PERFORMANCE"

            message = f"{action_name} took {duration:.2f} seconds"
            logger.log(log_level, message, extra={"tag": tag})
            return result
        return wrapper
    return decorator

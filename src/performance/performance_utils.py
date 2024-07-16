from functools import wraps
import time
import logging


def measure_performance(action_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self = args[0]  # The first argument should be the test class instance
            logger = self.logger  # Access the logger from the test class instance
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time

            # Determine if the performance threshold is exceeded
            if duration > self.performance_thresholds.get(action_name, float('inf')):
                log_level = logging.WARNING
                tag = "PERFORMANCE WARNING"
                message = f"{action_name} took {duration:.2f} seconds"
            else:
                log_level = logging.getLevelName("PERFORMANCE")
                tag = "PERFORMANCE"
                message = f"{action_name} took {duration:.2f} seconds"

            logger.log(log_level, message, extra={"tag": tag})
            return result
        return wrapper
    return decorator

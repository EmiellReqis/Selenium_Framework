import logging
import os

# Define a custom log level for performance
PERFORMANCE = 25
logging.addLevelName(PERFORMANCE, "PERFORMANCE")


def performance(self, message, *args, **kwargs):
    """
        Custom log level for performance-related messages.

        :param message: Log message
        :param args: Additional arguments
        :param kwargs: Additional keyword arguments
        """
    if self.isEnabledFor(PERFORMANCE):
        self._log(PERFORMANCE, message, args, **kwargs)


logging.Logger.performance = performance


def get_logger(test_suite_name, test_name, base_dir):
    """
    Set up and get a logger for the specified test suite and test name.

    :param test_suite_name: Name of the test suite
    :param test_name: Name of the test
    :param base_dir: Base directory for logs
    :return: Logger instance
    """
    log_file = os.path.join(base_dir, f"{test_name}.log")

    logger = logging.getLogger(f"{test_suite_name}_{test_name}")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


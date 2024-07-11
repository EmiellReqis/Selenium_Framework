import logging
import os
from datetime import datetime


def get_logger(test_suite_name):
    """
    Set up and get a logger for the specified test suite.

    :param test_suite_name: Name of the test suite
    :return: Logger instance
    """
    # Get the current date and time
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H-%M-%S")

    # Get the directory one level above the current directory
    base_reports_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'reports'))

    # Define the path for the current date and time
    current_date_dir = os.path.join(base_reports_dir, current_date)
    current_suite_dir = os.path.join(current_date_dir, f"{test_suite_name}_{current_time}")

    # Create the directories if they don't exist
    os.makedirs(current_suite_dir, exist_ok=True)

    # Define the log file path
    log_file = os.path.join(current_suite_dir, f"{test_suite_name}.log")

    # Set up the logger
    logger = logging.getLogger(test_suite_name)
    logger.setLevel(logging.INFO)

    # Create a file handler for writing log messages to a file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Create a console handler for writing log messages to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

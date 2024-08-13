import os
from src.utils.screenshot_utils import capture_screenshot


def log_exception(logger, message, exc, screenshot_path=None):
    """
    Log an exception with an optional screenshot path.

    :param logger: Logger instance to log messages.
    :param message: Custom message to log.
    :param exc: Exception instance that was raised.
    :param screenshot_path: Path to the screenshot file, if available.
    """
    if screenshot_path:
        logger.error(f"{message}: {exc}. Screenshot saved to {screenshot_path}")
    else:
        logger.error(f"{message}: {exc}")


def handle_exception(logger, driver, exc, operation_name, page_name=None, locator_name=None):
    """
    Handles different types of exceptions and provides context-specific error handling.

    :param logger: Logger instance to log messages.
    :param driver: WebDriver instance to capture screenshots.
    :param exc: Exception instance that was raised.
    :param operation_name: Custom message to log and include in screenshot name.
    :param page_name: Name of the page where the error occurred.
    :param locator_name: Name of the locator involved in the operation.
    """
    screenshot_path = capture_screenshot(
        driver,
        os.path.dirname(logger.handlers[0].baseFilename),
        operation_name,
        page_name,
        locator_name
    )
    log_exception(logger, operation_name, exc, screenshot_path)


def retry_operation(operation, retries: int = 3, delay: int = 2, logger=None):
    """
    Retries a given operation multiple times before failing.

    Args:
        operation: Callable operation to retry.
        retries: Number of retries.
        delay: Delay between retries.
        logger: Logger instance for logging retry attempts.

    Returns:
        Result of the operation if successful.

    Raises:
        Exception: The last exception raised if all retries fail.
    """
    import time

    last_exception = None
    for attempt in range(retries):
        try:
            result = operation()
            if logger:
                logger.info(f"Operation succeeded on attempt {attempt + 1}")
            return result
        except Exception as e:
            last_exception = e
            if logger:
                logger.warning(f"Operation failed on attempt {attempt + 1}: {str(e)}")
            time.sleep(delay)
    if logger:
        logger.error(f"Operation failed after {retries} attempts")
    raise last_exception

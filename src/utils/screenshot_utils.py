import os
import re
import datetime


def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)


def capture_screenshot(driver, base_dir, operation_name=None, page_name=None, locator_name=None):
    """
    Capture a screenshot of the current state of the browser with a custom filename.

    :param driver: WebDriver instance
    :param base_dir: Directory to save the screenshot
    :param operation_name: Operation name that triggered the screenshot
    :param page_name: Name of the page where the error occurred
    :param locator_name: Name of the locator involved in the operation
    :return: Path to the screenshot file
    """
    # Sanitize names to ensure valid filenames
    sanitized_operation = sanitize_filename(operation_name) if operation_name else "operation"
    sanitized_page = sanitize_filename(page_name) if page_name else "page"
    sanitized_locator = sanitize_filename(locator_name) if locator_name else "locator"

    # Get current time to include in the screenshot name
    current_time = datetime.datetime.now().strftime("%H%M%S")

    # Create the filename
    screenshot_name = f"Failed_during_{sanitized_operation}_{sanitized_page}_{sanitized_locator}_{current_time}.png"

    # Create the directory structure
    screenshot_dir = os.path.join(base_dir, "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    # Create the full path for the screenshot
    screenshot_path = os.path.join(screenshot_dir, screenshot_name)

    # Capture the screenshot
    driver.save_screenshot(screenshot_path)

    return screenshot_path


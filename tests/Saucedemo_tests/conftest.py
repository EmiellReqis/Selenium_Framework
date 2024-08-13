import pytest
import os
from datetime import datetime
from src.utils.driver_factory import get_driver
from src.utils.logger import get_logger


@pytest.fixture(scope="class")
def class_logger(request):
    """
    Fixture to set up the logging directory for the test class.
    Creates a directory for the current date, site name, and test class.

    :param request: Pytest request object
    :return: Directory path for the test class logs
    """
    test_suite_name = os.getenv("TEST_SUITE_NAME", "Saucedemo")
    current_date = datetime.now().strftime("%Y-%m-%d")
    base_reports_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'reports'))
    test_class_dir = os.path.join(base_reports_dir, current_date, test_suite_name,
                                  f"{request.cls.__name__}_{datetime.now().strftime('%H-%M-%S')}")
    os.makedirs(test_class_dir, exist_ok=True)
    request.cls.test_class_dir = test_class_dir
    return test_class_dir


@pytest.fixture(scope="function")
def logger(request, class_logger):
    """
    Fixture to set up a logger for each test function.

    :param request: Pytest request object
    :param class_logger: Directory path for the test class logs
    :return: Logger instance for the test function
    """
    test_suite_name = os.getenv("TEST_SUITE_NAME", "Saucedemo")
    test_name = request.node.originalname if hasattr(request.node, 'originalname') else request.node.name
    test_class_dir = request.cls.test_class_dir
    logger = get_logger(test_suite_name, test_name, test_class_dir)
    return logger


@pytest.fixture(scope="function")
def driver():
    """
    Fixture to set up the WebDriver instance.

    :return: WebDriver instance
    """
    driver = get_driver()
    yield driver
    driver.quit()

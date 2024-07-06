import pytest
from src.utils.driver_factory import get_driver
from src.utils.logger import get_logger


@pytest.fixture(scope="session")
def logger():
    return get_logger("Saucedemo_tests")


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
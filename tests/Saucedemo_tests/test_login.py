import pytest
from src.pages.landing_page import LandingPage
from src.pages.login_page import LoginPage
from src.utils.driver_factory import get_driver
from src.utils.config_loader import load_config
from src.utils.logger import get_logger

logger = get_logger("Saucedemo_tests")

# Load configuration
config = load_config()


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_valid_login(driver):
    logger.info("Starting test: test_valid_login")
    site_name = 'saucedemo'
    landing_page = LandingPage(driver, config['sites'][site_name]['base_url'], site_name, logger)
    login_page = LoginPage(driver, site_name, logger)

    landing_page.open()
    login_page.login(config["sites"]["saucedemo"]["usernames"][0], config["sites"]["saucedemo"]["password"])
    assert login_page.is_logged_in()
    logger.info("Test test_valid_login passed")

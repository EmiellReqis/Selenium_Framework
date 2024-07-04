import pytest
from src.pages.landing_page import LandingPage
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
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


def test_add_items_to_cart(driver):
    logger.info("Starting test: test_add_items_to_cart")
    site_name = 'saucedemo'
    landing_page = LandingPage(driver, config['sites'][site_name]['base_url'], site_name, logger)
    login_page = LoginPage(driver, site_name, logger)
    home_page = HomePage(driver, site_name, logger)

    landing_page.open()
    login_page.login(config["sites"]["saucedemo"]["usernames"][0], config["sites"]["saucedemo"]["password"])
    assert login_page.is_logged_in()
    logger.info("Logged in")

    home_page.add_item_to_cart('backpack')
    home_page.add_item_to_cart('bike_light')
    home_page.add_item_to_cart('t_shirt')
    home_page.add_item_to_cart('jacket')
    home_page.add_item_to_cart('onesie')
    home_page.add_item_to_cart('red_t_shirt')
    assert home_page.is_item_in_cart(6)
    logger.info("Test test_add_to_cart passed")
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
    logger.info("Items added to cart")

    home_page.remove_item_from_cart('backpack')
    assert home_page.is_item_in_cart(5)
    home_page.remove_item_from_cart('bike_light')
    assert home_page.is_item_in_cart(4)
    home_page.remove_item_from_cart('t_shirt')
    assert home_page.is_item_in_cart(3)
    home_page.remove_item_from_cart('jacket')
    assert home_page.is_item_in_cart(2)
    home_page.remove_item_from_cart('onesie')
    assert home_page.is_item_in_cart(1)
    home_page.remove_item_from_cart('red_t_shirt')
    assert home_page.is_cart_empty()
    logger.info("Test test_remove_from_cart passed")

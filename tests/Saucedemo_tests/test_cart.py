import pytest
from src.pages.landing_page import LandingPage
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.utils.config_loader import load_config

# Load configuration
config = load_config()


class TestCart:

    @pytest.fixture(autouse=True)
    def setup(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.site_name = 'saucedemo'

        self.landing_page = LandingPage(driver, config['sites'][self.site_name]['base_url'], self.site_name, self.logger)
        self.login_page = LoginPage(driver, self.site_name, self.logger)
        self.home_page = HomePage(driver, self.site_name, self.logger)

        # Perform initial login
        self.landing_page.open()
        self.login_page.login(config["sites"]["saucedemo"]["usernames"][0], config["sites"]["saucedemo"]["password"])
        assert self.login_page.is_logged_in()
        self.logger.info("Logged in")
        self.logger.info("Initial setup completed")

    @pytest.mark.parametrize("item_name", [
        'backpack',
        'bike_light',
        't_shirt',
        'jacket',
        'onesie',
        'red_t_shirt'
    ])
    def test_add_item_to_cart(self, item_name, logger):
        self.logger.info("Starting test: test_add_item_to_cart")
        self.home_page.add_item_to_cart(item_name)
        assert self.home_page.is_item_in_cart(1), f"{item_name} was not added to cart"
        self.logger.info("Test test_add_item_to_cart passed")

    @pytest.mark.parametrize("items", [
        ['backpack', 'bike_light', 't_shirt', 'jacket', 'onesie', 'red_t_shirt']
    ])
    def test_add_multiple_items_to_cart(self, items, logger):
        self.logger.info("Starting test: test_add_multiple_items_to_cart")
        for count, item in enumerate(items, start=1):
            self.home_page.add_item_to_cart(item)
            assert self.home_page.is_item_in_cart(count), f"{item} was not added to cart"
        self.logger.info("Test test_add_multiple_items_to_cart passed")

    @pytest.mark.parametrize("items", [
        ['backpack', 'bike_light', 't_shirt', 'jacket', 'onesie', 'red_t_shirt']
    ])
    def test_remove_from_cart(self, items, logger):
        self.logger.info("Starting test: test_remove_from_cart")

        # Add items to cart first
        for count, item in enumerate(items, start=1):
            self.home_page.add_item_to_cart(item)
            assert self.home_page.is_item_in_cart(count), f"{item} was not added to cart"
            self.logger.info(f"{item} added to cart successfully")

        # Remove items from cart
        for index, item in enumerate(items):
            self.home_page.remove_item_from_cart(item)
            remaining_items = len(items) - index - 1
            if remaining_items > 0:
                assert self.home_page.is_item_in_cart(remaining_items), f"{item} was not removed from cart"
            else:
                assert self.home_page.is_cart_empty(), "Cart is not empty after removing all items"

        self.logger.info(f"All items {items} removed from cart successfully")
        self.logger.info("Test test_remove_from_cart passed")
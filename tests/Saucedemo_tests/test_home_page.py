import pytest
from src.pages.landing_page import LandingPage
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.utils.config_loader import load_config
from src.performance.performance_utils import measure_performance
from src.performance.performance_thresholds import performance_thresholds

# Load configuration
config = load_config()


class TestHomePage:

    @pytest.fixture(autouse=True)
    def setup(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.site_name = 'saucedemo'
        self.performance_thresholds = performance_thresholds

        self.landing_page = LandingPage(driver, config['sites'][self.site_name]['base_url'], self.site_name, self.logger)
        self.login_page = LoginPage(driver, self.site_name, self.logger)
        self.home_page = HomePage(driver, config['sites'][self.site_name]['base_url'], self.site_name, self.logger)

        self.logger.info('Start test setup')
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
    @measure_performance('Cart Process')
    def test_add_item_to_cart(self, item_name, logger):
        self.logger.info("Starting test: test_add_item_to_cart")
        self.home_page.add_item_to_cart(item_name)
        assert self.home_page.is_item_in_cart(1), f"{item_name} was not added to cart"
        self.logger.info("Test test_add_item_to_cart passed")

    @pytest.mark.parametrize("items", [
        ['backpack', 'bike_light', 't_shirt', 'jacket', 'onesie', 'red_t_shirt']
    ])
    @measure_performance('Cart Process')
    def test_add_multiple_items_to_cart(self, items, logger):
        self.logger.info("Starting test: test_add_multiple_items_to_cart")
        for count, item in enumerate(items, start=1):
            self.home_page.add_item_to_cart(item)
            assert self.home_page.is_item_in_cart(count), f"{item} was not added to cart"
        self.logger.info("Test test_add_multiple_items_to_cart passed")

    @pytest.mark.parametrize("items", [
        ['backpack', 'bike_light', 't_shirt', 'jacket', 'onesie', 'red_t_shirt']
    ])
    @measure_performance('Cart Process')
    def test_remove_from_cart(self, items, logger):
        self.logger.info("Starting test: test_remove_from_cart")

        # Add items to cart first
        for count, item in enumerate(items, start=1):
            self.home_page.add_item_to_cart(item)
            assert self.home_page.is_item_in_cart(count), f"{item} was not added to cart"

        # Remove items from cart
        for index, item in enumerate(items):
            self.home_page.remove_item_from_cart(item)
            remaining_items = len(items) - index - 1
            if remaining_items > 0:
                assert self.home_page.is_item_in_cart(remaining_items), f"{item} was not removed from cart"
            else:
                assert self.home_page.is_cart_empty(), "Cart is not empty after removing all items"

        self.logger.info("Test test_remove_from_cart passed")

    @pytest.mark.parametrize("sort_option, expected_text", [
        ('a_z', 'name (a to z)'),
        ('z_a', 'name (z to a)'),
        ('low_to_high', 'price (low to high)'),
        ('high_to_low', 'price (high to low)')
    ])
    @measure_performance('Sort Process')
    def test_sort_items(self, sort_option, expected_text, logger):
        self.logger.info("Starting test: test_sort_items")
        self.home_page.sort_order_choose(sort_option)
        sort_text = self.home_page.sort_order_text(sort_option)
        self.logger.info(f"Sort order text: {sort_text}")
        assert sort_text.lower() == expected_text, f"Expected {expected_text} but got '{sort_text}'"
        self.logger.info("Test passed")

    @pytest.mark.parametrize("item_name, name_in_about_item_page, item_price", [
        ('backpack', 'Sauce Labs Backpack', '$29.99'),
        ('bike_light', 'Sauce Labs Bike Light', '$9.99'),
        ('t_shirt', 'Sauce Labs Bolt T-Shirt', '$15.99'),
        ('jacket', 'Sauce Labs Fleece Jacket', '$49.99'),
        ('onesie', 'Sauce Labs Onesie', '$7.99'),
        ('red_t_shirt', 'Test.allTheThings() T-Shirt (Red)', '$15.99')
    ])
    @measure_performance('About Item Process')
    def test_about_item_pages(self, item_name, name_in_about_item_page, item_price, logger):
        self.logger.info("Starting test: test_about_item_pages")
        self.home_page.about_item(item_name)
        assert self.home_page.get_element_text(self.home_page.get_locator('about_item_page')) == name_in_about_item_page
        assert self.home_page.get_element_text(self.home_page.get_locator('item_price')) == item_price
        self.logger.info("Test test_about_item_pages passed")

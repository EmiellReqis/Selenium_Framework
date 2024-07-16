import pytest
from src.pages.landing_page import LandingPage
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.cart_page import CartPage
from src.utils.config_loader import load_config
from src.performance.performance_utils import measure_performance
from src.performance.performance_thresholds import performance_thresholds

# Load configuration
config = load_config()


class TestCartPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.site_name = 'saucedemo'

        self.landing_page = LandingPage(driver, config['sites'][self.site_name]['base_url'], self.site_name, self.logger)
        self.login_page = LoginPage(driver, self.site_name, self.logger)
        self.home_page = HomePage(driver, self.site_name, self.logger)
        self.cart_page = CartPage(driver, self.site_name, self.logger)
        self.performance_thresholds = performance_thresholds

        # Perform initial login
        self.landing_page.open()
        self.login_page.login(config["sites"]["saucedemo"]["usernames"][0], config["sites"]["saucedemo"]["password"])
        assert self.login_page.is_logged_in()
        self.logger.info("Logged in")
        self.logger.info("Initial setup completed")

    @measure_performance('Checkout Process')
    def test_go_to_checkout(self, logger):
        self.logger.info("Starting test: test_go_to_checkout")
        self.home_page.click(self.home_page.locators['cart']['go_to_cart'])
        self.cart_page.click(self.cart_page.locators['checkout']['checkout_button'])
        assert self.cart_page.get_checkout_page_status() == "Checkout: Your Information"
        self.logger.info("Test test_go_to_checkout passed")

    @measure_performance('Checkout Process')
    def test_write_credentials(self, logger):
        self.logger.info("Starting test: test_write_credentials")
        self.home_page.click(self.home_page.locators['cart']['go_to_cart'])
        self.cart_page.click(self.cart_page.locators['checkout']['checkout_button'])
        assert self.cart_page.get_checkout_page_status() == "Checkout: Your Information"
        self.cart_page.write_credentials('John', 'Smith', '12-123')
        assert self.cart_page.get_checkout_page_status() == "Checkout: Overview"
        self.cart_page.click(self.cart_page.locators['checkout']['checkout_finish'])
        assert self.cart_page.wait_for_element(self.cart_page.locators["back_to_home_button"])
        self.logger.info("Test test_write_credentials passed")

    @pytest.mark.parametrize("first_name, last_name, zip_code, message", [
        ('', 'Smith', '12-123', 'Error: First Name is required'),
        ('John', '', '12-123', 'Error: Last Name is required'),
        ('John', 'Smith', '', 'Error: Postal Code is required')
    ])
    @measure_performance('Checkout Process')
    def test_missing_credentials(self, logger, first_name, last_name, zip_code, message):
        self.logger.info("Starting test: test_missing_credentials")
        self.home_page.click(self.home_page.locators['cart']['go_to_cart'])
        self.cart_page.click(self.cart_page.locators['checkout']['checkout_button'])
        assert self.cart_page.get_checkout_page_status() == "Checkout: Your Information"
        self.cart_page.write_credentials(first_name, last_name, zip_code)
        error_message = self.cart_page.get_error_message(self.cart_page.locators['error_note'])
        expected_message = message
        assert error_message == expected_message, f"Expected '{expected_message}' but got '{error_message}'"
        self.logger.info("Test test_missing_credentials passed")


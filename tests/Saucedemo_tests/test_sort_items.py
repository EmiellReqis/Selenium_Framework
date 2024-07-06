import pytest
from src.pages.landing_page import LandingPage
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.utils.config_loader import load_config

# Load configuration
config = load_config()


class TestSortItems:

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

    @pytest.mark.parametrize("sort_option, expected_text", [
        ('a_z', 'name (a to z)'),
        ('z_a', 'name (z to a)'),
        ('low_to_high', 'price (low to high)'),
        ('high_to_low', 'price (high to low)')
    ])
    def test_sort_items(self, sort_option, expected_text,logger):
        self.logger.info("Starting test: test_sort_items")
        self.home_page.sort_order_choose(sort_option)
        sort_text = self.home_page.sort_order_text(sort_option)
        self.logger.info(f"Sort order text: {sort_text}")
        assert sort_text.lower() == expected_text, f"Expected {expected_text} but got '{sort_text}'"
        self.logger.info("Test passed")

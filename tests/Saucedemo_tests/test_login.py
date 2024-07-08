import pytest
from src.pages.landing_page import LandingPage
from src.pages.login_page import LoginPage
from src.pages.base_page import BasePage
from src.utils.config_loader import load_config

# Load configuration
config = load_config()


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.site_name = 'saucedemo'

        self.landing_page = LandingPage(driver, config['sites'][self.site_name]['base_url'], self.site_name, self.logger)
        self.login_page = LoginPage(driver, self.site_name, self.logger)

        self.landing_page.open()

    @pytest.mark.parametrize("username", [
        'standard_user',
        'problem_user',
        'performance_glitch_user',
        'error_user',
        'visual_user'
    ])
    def test_valid_login(self, username, logger):
        self.logger.info("Starting test: test_valid_login")
        self.login_page.login(username, config["sites"]["saucedemo"]["password"])
        assert self.login_page.is_logged_in()
        self.logger.info(f"Logged in as: {username}")
        self.logger.info("Test test_valid_login passed")

    @pytest.mark.parametrize("username, password, message", [
        ('locked_out_user', 'secret_sauce', 'Epic sadface: Sorry, this user has been locked out.'),
        ('invalid_username', 'secret_sauce',
         'Epic sadface: Username and password do not match any user in this service'),
        ('locked_out_user', 'invalid_password',
         'Epic sadface: Username and password do not match any user in this service')
    ] )
    def test_invalid_login(self, username, password, message, logger):
        self.logger.info("Starting test: test_invalid_login")
        self.login_page.login(username, password)
        error_message = self.login_page.login_error()
        expected_message = message
        assert error_message == expected_message, f"Expected '{expected_message}' but got '{error_message}'"
        self.logger.info("Test test_invalid_login passed")
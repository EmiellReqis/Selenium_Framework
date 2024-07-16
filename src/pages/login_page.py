from selenium.webdriver.remote.webdriver import WebDriver
from src.pages.base_page import BasePage
from src.utils.locator_loader import load_locators


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver, site_name: str, logger):
        """
        Initialize the LoginPage with a driver, site name, and logger.

        :param driver: WebDriver instance
        :param site_name: Name of the site
        :param logger: Logger instance
        """
        locators = load_locators(site_name, 'login_page')['LoginPage']
        super().__init__(driver, locators, logger)

    def login(self, username: str, password: str):
        """
        Perform the login action using the provided username and password.

        :param username: Username for login
        :param password: Password for login
        """
        self.type(self.locators['username_field'], username)
        self.type(self.locators['password_field'], password)
        self.click(self.locators['login_button'])

    def is_logged_in(self) -> bool:
        """
        Check if the login was successful.

        :return: True if logged in, False otherwise
        """
        return self.wait_for_element(self.locators['logged_in_element']).is_displayed()

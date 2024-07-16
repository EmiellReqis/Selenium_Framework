from selenium.webdriver.remote.webdriver import WebDriver
from src.pages.base_page import BasePage
from src.utils.locator_loader import load_locators


class CartPage(BasePage):
    def __init__(self, driver: WebDriver, site_name: str, logger):
        """
        Initialize the CartPage with a driver, site name, and logger.

        :param driver: WebDriver instance
        :param site_name: Name of the site
        :param logger: Logger instance
        """
        locators = load_locators(site_name, 'cart_page')['CartPage']
        super().__init__(driver, locators, logger)

    def get_checkout_page_status(self):
        checkout_title_text = self.get_element_text(self.locators['checkout']['checkout_title'])
        return checkout_title_text

    def write_credentials(self, first_name: str = '', last_name: str = '', zip_code: str = ''):
        self.type(self.locators['checkout']['checkout_first_name'], first_name)
        self.type(self.locators['checkout']['checkout_last_name'], last_name)
        self.type(self.locators['checkout']['checkout_zip_code'], zip_code)
        self.click(self.locators['checkout']['checkout_continue'])

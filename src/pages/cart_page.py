from selenium.webdriver.remote.webdriver import WebDriver
from src.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver: WebDriver, site_name: str, logger):
        """
        Initialize the CartPage with a driver, site name, and logger.

        :param driver: WebDriver instance
        :param site_name: Name of the site
        :param logger: Logger instance
        """
        super().__init__(driver, site_name,  'cart_page', logger)

    def get_checkout_page_status(self):
        return self.get_element_text(self.get_locator('checkout', 'checkout_title'))

    def write_credentials(self, first_name: str = '', last_name: str = '', zip_code: str = ''):
        self.type(self.get_locator('checkout', 'checkout_first_name'), first_name)
        self.type(self.get_locator('checkout', 'checkout_last_name'), last_name)
        self.type(self.get_locator('checkout', 'checkout_zip_code'), zip_code)
        self.click(self.get_locator('checkout', 'checkout_continue'))

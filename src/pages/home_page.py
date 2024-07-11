from src.pages.base_page import BasePage
from src.utils.locator_loader import load_locators
from selenium.webdriver.common.by import By
import time


class HomePage(BasePage):
    def __init__(self, driver, site_name, logger):
        """
        Initialize the HomePage with a driver, site name, and logger.

        :param driver: WebDriver instance
        :param site_name: Name of the site
        :param logger: Logger instance
        """
        locators = load_locators(site_name, 'home_page')['HomePage']
        # self.logger = logger
        super().__init__(driver, locators, logger)

    def about_item(self, item_name):
        """
        Click on the item information based on the item name.

        :param item_name: Name of the item
        """
        item = next(item for item in self.locators['items'] if item['item_name'] == item_name)
        self.click(item['item_info'])

    def add_item_to_cart(self, item_name):
        """
        Add an item to the cart based on the item name.

        :param item_name: Name of the item
        """
        item = next(item for item in self.locators['items'] if item['item_name'] == item_name)
        self.click(item['add_to_cart'])
        self.logger.info(f"{item_name} added to cart successfully")

    def remove_item_from_cart(self, item_name):
        """
        Remove an item from the cart based on the item name.

        :param item_name: Name of the item
        """
        item = next(item for item in self.locators['items'] if item['item_name'] == item_name)
        self.click(item['remove_from_cart'])
        self.logger.info(f"{item_name} removed from cart successfully")

    def is_item_in_cart(self, count):
        """
        Check if the number of items in the cart matches the expected count.

        :param count: Expected number of items in the cart
        :return: True if the count matches, False otherwise
        """
        cart_count_locator = f"//span[@class='shopping_cart_badge'][contains(text(),'{count}')]"
        return self.wait_for_element({'type': 'xpath', 'value': cart_count_locator}).is_displayed()

    def go_to_cart(self):
        """
        Navigate to the cart page.
        """
        self.click(self.locators['cart_link'])

    def is_cart_empty(self):
        """
        Check if the cart is empty.

        :return: True if the cart is empty, False otherwise
        """
        try:
            self.wait_for_element((By.XPATH, "//span[@class='shopping_cart_badge']"), timeout=5)
            self.logger.info(f"Cart is empty")
            return False
        except:
            return True

    def sort_order_choose(self, sort_option):
        """
        Choose the sort order for items based on the given option.

        :param sort_option: Sort option to choose
        """
        self.click(self.locators['sort_list'][sort_option])
        self.logger.info(f"Items sorted: {sort_option}")

    def sort_order_text(self, sort_option):
        """
        Get the text of the sort order based on the given option.

        :param sort_option: Sort option to get the text of
        :return: The sort order text
        """
        sort_order_text = self.get_element_text(self.locators['sort_list'][sort_option])
        return sort_order_text

    def logout(self):
        """
        Logs out the user from the application.
        """
        self.click(self.locators['menu_logout']['menu_button'])
        self.click(self.locators['menu_logout']['logout'])
        self.logger.info("Logged out successfully")

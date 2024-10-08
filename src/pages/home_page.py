from src.pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class HomePage(BasePage):
    def __init__(self, driver: WebDriver, base_url: str, site_name: str, logger):
        """
        Initialize the HomePage with a driver, site name, and logger.

        :param driver: WebDriver instance
        :param site_name: Name of the site
        :param logger: Logger instance
        """
        super().__init__(driver, site_name, 'home_page', logger)
        self.base_url = base_url

    def about_item(self, item_name: str):
        """
        Click on the item information based on the item name.

        :param item_name: Name of the item
        """
        self.click(self.get_locator('items', item_name, 'item_info'))

    def add_item_to_cart(self, item_name: str):
        """
        Add an item to the cart based on the item name.

        :param item_name: Name of the item
        """
        self.click(self.get_locator('items', item_name, 'add_to_cart'))
        self.logger.info(f"{item_name} added to cart successfully")

    def remove_item_from_cart(self, item_name: str):
        """
        Remove an item from the cart based on the item name.

        :param item_name: Name of the item
        """
        self.click(self.get_locator('items', item_name, 'remove_from_cart'))
        self.logger.info(f"{item_name} removed from cart successfully")

    def is_item_in_cart(self, count: int) -> bool:
        """
        Check if the number of items in the cart matches the expected count.

        :param count: Expected number of items in the cart
        :return: True if the count matches, False otherwise
        """
        cart_count_locator = f"//span[@class='shopping_cart_badge'][contains(text(),'{count}')]"
        return self.wait_for_element({'type': 'xpath', 'value': cart_count_locator}).is_displayed()

    def is_cart_empty(self) -> bool:
        """
        Check if the cart is empty.

        :return: True if the cart is empty, False otherwise
        """
        try:
            self.wait_for_element({'type': 'xpath', 'value': "//span[@class='shopping_cart_badge']"}, timeout=5)
            self.logger.info("Cart is not empty")
            return False
        except:
            self.logger.info("Cart is empty")
            return True

    def sort_order_choose(self, sort_option):
        """
        Choose the sort order for items based on the given option.

        :param sort_option: Sort option to choose
        """
        self.click(self.get_locator('sort_list', sort_option))
        self.logger.info(f"Items sorted: {sort_option}")

    def sort_order_text(self, sort_option: str) -> str:
        """
        Get the text of the sort order based on the given option.

        :param sort_option: Sort option to get the text of
        :return: The sort order text
        """
        return self.get_element_text(self.get_locator('sort_list', sort_option))

    def logout(self):
        """
        Logs out the user from the application.
        """
        self.click(self.get_locator('menu', 'menu_button'))
        self.click(self.get_locator('menu', 'logout'))
        self.logger.info("Logged out successfully")

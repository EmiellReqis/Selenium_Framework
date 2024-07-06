from src.pages.base_page import BasePage
from src.utils.locator_loader import load_locators
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, driver, site_name, logger):
        locators = load_locators(site_name, 'home_page')['HomePage']
        # self.logger = logger
        super().__init__(driver, locators, logger)

    def about_item(self, item_name):
        item = next(item for item in self.locators['items'] if item['item_name'] == item_name)
        self.click(item['item_info'])

    def add_item_to_cart(self, item_name):
        item = next(item for item in self.locators['items'] if item['item_name'] == item_name)
        self.click(item['add_to_cart'])
        self.logger.info(f"{item_name} added to cart successfully")

    def remove_item_from_cart(self, item_name):
        item = next(item for item in self.locators['items'] if item['item_name'] == item_name)
        self.click(item['remove_from_cart'])
        self.logger.info(f"{item_name} removed from cart successfully")

    def is_item_in_cart(self, count):
        cart_count_locator = f"//span[@class='shopping_cart_badge'][contains(text(),'{count}')]"
        return self.wait_for_element({'type': 'xpath', 'value': cart_count_locator}).is_displayed()

    def go_to_cart(self):
        self.click(self.locators['cart_link'])

    def is_cart_empty(self):
        try:
            self.wait_for_element((By.XPATH, "//span[@class='shopping_cart_badge']"), timeout=5)
            self.logger.info(f"Cart is empty")
            return False
        except:
            return True

    def sort_order_choose(self, sort_option):
        self.click(self.locators['sort_list'][sort_option])
        self.logger.info(f"Items sorted: {sort_option}")

    def sort_order_text(self, sort_option):
        sort_order_text = self.get_element_text(self.locators['sort_list'][sort_option])
        return sort_order_text

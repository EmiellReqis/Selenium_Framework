from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.logger import get_logger


class BasePage:
    def __init__(self, driver, locators, logger):
        self.driver = driver
        self.locators = locators
        self.logger = logger

    def wait_for_element(self, locator, timeout=10):
        by_type = locator['type']
        value = locator['value']
        self.logger.info(f"Waiting for element by {by_type} with value {value} for {timeout} seconds")
        if by_type == 'xpath':
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by_type, value)))
        # Add more conditions for other locator types if needed

    def click(self, locator):
        self.logger.info(f"Clicking element by {locator['type']} with value {locator['value']}")
        self.wait_for_element(locator).click()

    def type(self, locator, text):
        self.logger.info(f"Typing text '{text}' into element by {locator['type']} with value {locator['value']}")
        self.wait_for_element(locator).send_keys(text)
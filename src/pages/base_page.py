from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import Dict, Any


class BasePage:
    def __init__(self, driver: WebDriver, locators: Dict[str, Any], logger, timeout: int = 10):
        """
        Initialize the BasePage with a driver, locators, and logger.

        :param driver: WebDriver instance
        :param locators: Dictionary of locators
        :param logger: Logger instance
        :param timeout: Default timeout for waiting for elements
        """
        self.driver = driver
        self.locators = locators
        self.logger = logger
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, locator: Dict[str, str], timeout: int = 10) -> WebElement:
        """
        Wait for an element to be present on the page.

        :param locator: Dictionary with 'type' and 'value' keys
        :param timeout: Maximum time to wait for the element
        :return: WebElement once it is located
        """
        by_type = locator['type']
        value = locator['value']
        self.logger.info(f"Waiting for element by {by_type} with value {value} for {timeout} seconds")
        if by_type == 'xpath':
            return self.wait.until(EC.presence_of_element_located((By.XPATH, value)))
        elif by_type == 'id':
            return self.wait.until(EC.presence_of_element_located((By.ID, value)))
        elif by_type == 'name':
            return self.wait.until(EC.presence_of_element_located((By.NAME, value)))
            # Add more conditions for other locator types if needed
        else:
            raise ValueError(f"Unsupported locator type: {by_type}")

    def click(self, locator: Dict[str, str], timeout: int = 10):
        """
        Click on an element located by the given locator.

        :param locator: Dictionary with 'type' and 'value' keys
        :param timeout: Maximum time to wait for the element
        """
        by_type = locator['type']
        value = locator['value']
        self.logger.info(f"Waiting to click element by {by_type} with value {value} for {timeout} seconds")
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, value)))
        element.click()

    def type(self, locator: Dict[str, str], text: str):
        """
        Type text into an element located by the given locator.

        :param locator: Dictionary with 'type' and 'value' keys
        :param text: Text to type into the element
        """
        self.logger.info(f"Typing text '{text}' into element by {locator['type']} with value {locator['value']}")
        self.wait_for_element(locator).send_keys(text)

    def get_element_text(self, locator: Dict[str, str]) -> str:
        """
        Get the text of an element located by the given locator.

        :param locator: Dictionary with 'type' and 'value' keys
        :return: Text of the element
        """
        self.logger.info(f"Getting text of element by {locator['type']} with value {locator['value']}")
        element = self.wait_for_element(locator)
        element_text = element.text
        self.logger.info(f"Text of element: {element_text}")
        return element_text

    def get_error_message(self, locator: Dict[str, str]) -> str:
        """
        Get the error message text.

        :return: Text of the error message
        """
        self.logger.info(f"Getting error message of element by {locator['type']} "
                         f"with value {locator['value']}")
        return self.get_element_text(locator)

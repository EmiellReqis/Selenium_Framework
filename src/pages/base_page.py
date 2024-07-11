from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, locators, logger):
        """
        Initialize the BasePage with a driver, locators, and logger.

        :param driver: WebDriver instance
        :param locators: Dictionary of locators
        :param logger: Logger instance
        """
        self.driver = driver
        self.locators = locators
        self.logger = logger
        self.wait = WebDriverWait(driver, timeout=3)

    def wait_for_element(self, locator, timeout=10):
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

    def click(self, locator):
        """
        Click on an element located by the given locator.

        :param locator: Dictionary with 'type' and 'value' keys
        """
        by_type = locator['type']
        value = locator['value']
        self.logger.info(f"Clicking element by {by_type} with value {value}")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, value))).click()

    def type(self, locator, text):
        """
        Type text into an element located by the given locator.

        :param locator: Dictionary with 'type' and 'value' keys
        :param text: Text to type into the element
        """
        self.logger.info(f"Typing text '{text}' into element by {locator['type']} with value {locator['value']}")
        self.wait_for_element(locator).send_keys(text)

    def get_element_text(self, locator):
        """
        Get the text of an element located by the given locator.

        :param locator: Dictionary with 'type' and 'value' keys
        :return: Text of the element
        """
        self.logger.info(f"Getting text of element by {locator['type']} with value {locator['value']}")
        self.wait_for_element(locator)
        element_text = self.driver.find_element(locator['type'], locator['value']).text
        self.logger.info(f"Text of element: {element_text}")
        return element_text

from selenium.webdriver.remote.webdriver import WebDriver
from src.pages.base_page import BasePage


class LandingPage(BasePage):
    def __init__(self, driver: WebDriver, base_url: str, site_name: str, logger):
        """
        Initialize the LandingPage with a driver, base URL, site name, and logger.

        :param driver: WebDriver instance
        :param base_url: Base URL of the landing page
        :param site_name: Name of the site
        :param logger: Logger instance
        """
        super().__init__(driver, site_name, 'landing_page', logger)
        self.base_url = base_url

    def open(self):
        """
        Open the landing page.
        """
        self.logger.info("Opening landing page")
        self.driver.get(self.base_url)

    def navigate_to_home_page(self):
        """
        Navigate to the home page if a home button is present.
        """
        if 'home_button' in self.locators:
            self.logger.info("Navigating to home page")
            self.click(self.get_locator('home_button'))
        else:
            self.logger.info("Home button not found. Assuming already on home page.")

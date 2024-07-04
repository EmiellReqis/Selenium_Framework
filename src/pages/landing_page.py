from src.pages.base_page import BasePage
from src.utils.locator_loader import load_locators


class LandingPage(BasePage):
    def __init__(self, driver, base_url, site_name, logger):
        locators = load_locators(site_name, 'landing_page')['LandingPage']
        super().__init__(driver, locators, logger)
        self.base_url = base_url

    def open(self):
        self.logger.info("Opening landing page")
        self.driver.get(self.base_url)

    def navigate_to_home_page(self):
        if 'home_button' in self.locators:
            self.logger.info("Navigating to home page")
            self.click(self.locators['home_button'])
        else:
            self.logger.info("Home button not found. Assuming already on home page.")

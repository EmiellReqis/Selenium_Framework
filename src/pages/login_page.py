from src.pages.base_page import BasePage
from src.utils.locator_loader import load_locators


class LoginPage(BasePage):
    def __init__(self, driver, site_name, logger):
        locators = load_locators(site_name, 'login_page')['LoginPage']
        super().__init__(driver, locators, logger)

    def login(self, username, password):
        self.type(self.locators['username_field'], username)
        self.type(self.locators['password_field'], password)
        self.click(self.locators['login_button'])

    def is_logged_in(self):
        return self.wait_for_element(self.locators['logged_in_element']).is_displayed()

    def login_error(self):
        return self.get_element_text(self.locators["error_note"])

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):
    """Class that models the Login Page"""
    # LOCATORS
    _USERNAME = (By.CSS_SELECTOR, '[name="username"]')
    _PASSWORD = (By.CSS_SELECTOR, '[name="password"]')
    _LOGIN = (By.XPATH, '// button[contains(@class , "login")]')

    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self, username: str, password: str):
        self.enter_text(self._USERNAME, username)
        self.enter_text(self._PASSWORD, password)
        self.click(self._LOGIN)

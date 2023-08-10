from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self._driver = driver

    def wait_until_element_is_visible(self, locator: tuple):
        return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(locator))

    def wait_until_all_elements_are_visible(self, locator: tuple):
        return WebDriverWait(self._driver, 10).until((EC.visibility_of_all_elements_located(locator)))

    def enter_text(self, locator: tuple, text: str):
        self.wait_until_element_is_visible(locator).send_keys(text)

    def go_to(self, url: str):
        self._driver.get(url)

    def click(self, locator: tuple):
        self.wait_until_element_is_visible(locator).click()

    def get_elements(self, locator: tuple):
        return self.wait_until_all_elements_are_visible(locator)

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class RowNotFoundException(Exception):
    """Raised when the row with given value was not found """
    pass


class Table(object):
    """Models the table oject and its actions """
    # Default Locators
    _TABLE = (By.CSS_SELECTOR, 'div[role="table"]')
    _HEADER = (By.CSS_SELECTOR, 'div[role="columnheader"]')
    _BODY = (By.CSS_SELECTOR, 'div.oxd-table-body')
    _ROW = (By.CSS_SELECTOR, 'div.oxd-table-card')
    _CELL = (By.CSS_SELECTOR, 'div[role="cell"]')

    def __init__(self, driver, table_locators: dict = None):
        self._driver = driver
        self._actions_locators = {}
        if table_locators:
            self.set_table_locators(table_locators)

    @property
    def actions_locators(self):
        return self._actions_locators

    @actions_locators.setter
    def actions_locators(self, locators: dict):
        self._actions_locators.update(locators)

    def set_table_locators(self, locators: dict):
        for element, locator in locators.items():
            self.__setattr__(element, locator)

    def get_table(self) -> WebElement:
        return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(self._TABLE))

    def wait_until_table_loaded(self):
        return WebDriverWait(self._driver, 15).until(EC.visibility_of_element_located(self._HEADER))

    def get_column_names(self) -> list:
        headers = WebDriverWait(self._driver, 10).until(EC.visibility_of_all_elements_located(self._HEADER))
        column_names = [header.text for header in headers]
        return column_names

    def get_rows(self) -> list:
        return WebDriverWait(self._driver, 10).until(EC.visibility_of_all_elements_located(self._ROW))

    def get_column_id(self, column_name: str):
        return self.get_column_names().index(column_name)

    def cell_exists(self, column_name: str, value: str) -> bool:
        return True if self.get_row_with_value(column_name, value) else False

    def get_row_with_value(self, column_name: str, value: str) -> WebElement:
        rows = self.get_rows()
        column_id = self.get_column_id(column_name)
        for row in rows:
            cell = row.find_elements(self._CELL[0], self._CELL[1])[column_id]
            if cell.text == value:
                return row

    def click_on_action_on_row(self, column_name: str, value: str, action_name: str):
        row = self.get_row_with_value(column_name, value)
        if row:
            column_id = self.get_column_id('Actions')
            action_locator = self.actions_locators[action_name]
            action_element = row.find_element(action_locator[0], action_locator[1])
            try:
                action_element.click()
            except ElementClickInterceptedException:
                self._driver.execute_script('arguments[0].click()', action_element)
        else:
            raise RowNotFoundException(f'Row with column/value: ({column_name, value} not found!')


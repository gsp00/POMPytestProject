from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.Table import Table


class RecruitmentPage(BasePage):
    """Class that models the Recruitment page """
    # Locators
    _ADD_CANDIDATE = (By.XPATH, "//button[text()=' Add ']")
    _NAME = (By.NAME, "firstName")
    _LASTNAME = (By.NAME, "lastName")
    _EMAIL = (By.XPATH, "//div[label[text()='Email']]/following-sibling::div/input")
    _SAVE_CANDIDATE = (By.XPATH, "//button[text()=' Save ']")
    _CANDIDATE_NAME_COLUMN = (By.XPATH, "//div[@class='oxd-table-card']//div[3]")
    _DELETE_CONFIRM = (By.XPATH, "//button[text()=' Yes, Delete ']")
    _LOADING_INDICATOR = (By.CLASS_NAME, "oxd-loading-spinner")

    def __init__(self, driver):
        super(RecruitmentPage, self).__init__(driver)
        self._candidate_table = Table(driver)
        self.set_actions_table_locators()

    def set_actions_table_locators(self):
        actions_table_locators = {'view': (By.CSS_SELECTOR, "div.oxd-table-cell-actions button i.bi-eye-fill"),
                                  'delete': (By.XPATH, "//div[@class='oxd-table-cell-actions']"
                                                       "/button[i[@class='oxd-icon bi-trash']]"),
                                  'download': (By.CSS_SELECTOR, "div.oxd-table-cell-actions bi-download")}
        self._candidate_table.actions_locators.update(actions_table_locators)

    def click_add_candidate(self):
        self.click(self._ADD_CANDIDATE)

    def enter_candidate_name(self, text: str):
        self.enter_text(self._NAME, text)

    def enter_candidate_lastname(self, text: str):
        self.enter_text(self._LASTNAME, text)

    def enter_candidate_email(self, text: str):
        self.enter_text(self._EMAIL, text)

    def click_save_candidate(self):
        self.click(self._SAVE_CANDIDATE)

    def enter_basic_candidate_data(self, name: str, lastname: str, email: str):
        self.enter_candidate_name(name)
        self.enter_candidate_lastname(lastname)
        self.enter_candidate_email(email)

    def candidate_exists(self, fullname: str):
        exists = False
        elements = self.get_elements(self._CANDIDATE_NAME_COLUMN)
        for element in elements:
            if element.text == fullname:
                exists = True
                break
        return exists

    # TODO: remove for testing purposes only!
    def table_exists(self):
        return True if self._candidate_table.get_table() else False

    def column_exists(self, column_name: str):
        names = self._candidate_table.get_column_names()
        return True if column_name in names else False

    def column_id(self, column_name: str):
        index = self._candidate_table.get_column_id(column_name)
        return index

    def candidate_name_listed(self, fullname: str) -> bool:
        self._candidate_table.wait_until_table_loaded()
        return self._candidate_table.cell_exists('Candidate', fullname)

    def delete_candidate(self, fullname: str):
        self._candidate_table.click_on_action_on_row('Candidate', fullname, 'delete')
        self.wait_until_element_is_visible(self._DELETE_CONFIRM)
        self.click(self._DELETE_CONFIRM)
        self.wait_until_element_is_not_visible(self._DELETE_CONFIRM)
        self.wait_until_element_is_not_visible(self._LOADING_INDICATOR)



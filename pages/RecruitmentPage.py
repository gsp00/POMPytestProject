from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class RecruitmentPage(BasePage):
    """Class that models the Recruitment page """
    # Locators
    _ADD_CANDIDATE = (By.XPATH, "//button[text()=' Add ']")
    _NAME = (By.NAME, "firstName")
    _LASTNAME = (By.NAME, "lastName")
    _EMAIL = (By.XPATH, "//div[label[text()='Email']]/following-sibling::div/input")
    _SAVE_CANDIDATE = (By.XPATH, "//button[text()=' Save ']")
    _CANDIDATE_NAME_COLUMN = (By.XPATH, "//div[@class='oxd-table-card']//div[3]")

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

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.RecruitmentPage import RecruitmentPage


class MainMenu(BasePage):
    """Class that models the main menu of the application """
    # Locators
    _RECRUITMENT_MENU_ITEM = (By.LINK_TEXT, "Recruitment")
    _DASHBOARD_MENU_ITEM = (By.LINK_TEXT, "Dashboard")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_recruitment_menu(self):
        self.click(self._RECRUITMENT_MENU_ITEM)
        return RecruitmentPage(self._driver)

    def click_on_dashboard_menu(self):
        self.click(self._DASHBOARD_MENU_ITEM)


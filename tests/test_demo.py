import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.LoginPage import LoginPage
from pages.MainMenu import MainMenu

URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
DEFAULT_USER = {'username': 'Admin', 'password': 'admin123'}
CANDIDATE_DATA = {'name': 'test', 'lastname': 'flaky', 'email': 'tflaky@domain.com'}


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_one(driver):
    login_page = LoginPage(driver)
    main_menu = MainMenu(driver)

    login_page.do_login(DEFAULT_USER['username'], DEFAULT_USER['password'])
    recruitment_page = main_menu.click_on_recruitment_menu()
    # recruitment_page.click_add_candidate()
    # recruitment_page.enter_basic_candidate_data(**CANDIDATE_DATA)
    # recruitment_page.click_save_candidate()
    # main_menu.click_on_recruitment_menu()
    # fail_msg = f'Candidate with name {CANDIDATE_DATA["name"]} {CANDIDATE_DATA["lastname"]} was not found!!'
    # assert recruitment_page.candidate_exists(f'{CANDIDATE_DATA["name"]} {CANDIDATE_DATA["lastname"]}'), fail_msg
    recruitment_page.delete_candidate('test flaky')
    main_menu.click_on_recruitment_menu()
    time.sleep(5)










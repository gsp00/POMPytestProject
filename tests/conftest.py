import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from LoginPage import LoginPage

URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
DEFAULT_USER = {'username': 'Admin', 'password': 'admin123'}


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login_to_site(driver, url=URL):
    driver.get(url)
    login_page = LoginPage(driver)
    login_page.do_login(DEFAULT_USER['username'], DEFAULT_USER['password'])




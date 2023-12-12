import pytest
from faker import Faker

from pages.MainMenu import MainMenu


class TestDemo:
    @pytest.fixture
    def get_person(self):
        faker = Faker()
        self.candidate = {'name': faker.first_name(),
                          'lastname': faker.last_name(),
                          'email': faker.email()}

    @pytest.fixture
    def create_candidate(self, login_to_site, driver, get_person):
        self.main_menu = MainMenu(driver)
        self.recruitment_page = self.main_menu.click_on_recruitment_menu()
        self.recruitment_page.click_add_candidate()
        self.recruitment_page.enter_basic_candidate_data(**self.candidate)
        self.recruitment_page.click_save_candidate()
        self.main_menu.click_on_recruitment_menu()

    def test_add_candidate(self, login_to_site, driver, get_person):
        self.main_menu = MainMenu(driver)
        self.recruitment_page = self.main_menu.click_on_recruitment_menu()
        self.recruitment_page.click_add_candidate()
        self.recruitment_page.enter_basic_candidate_data(**self.candidate)
        self.recruitment_page.click_save_candidate()
        self.main_menu.click_on_recruitment_menu()

        fail_msg = f'Candidate with name {self.candidate["name"]} {self.candidate["lastname"]} was not found!!'
        assert self.recruitment_page.candidate_name_listed(f'{self.candidate["name"]} {self.candidate["lastname"]}'), fail_msg

    def test_delete_candidate(self, create_candidate):
        self.recruitment_page.delete_candidate(f'{self.candidate["name"]} {self.candidate["lastname"]}')
        self.main_menu.click_on_recruitment_menu()
        fail_msg = f'Candidate with name {self.candidate["name"]} {self.candidate["lastname"]} was found!!'
        candidate_exists = self.recruitment_page.candidate_name_listed(f'{self.candidate["name"]} {self.candidate["lastname"]}')
        assert candidate_exists is False, fail_msg


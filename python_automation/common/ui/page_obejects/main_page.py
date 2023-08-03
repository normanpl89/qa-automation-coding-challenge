from python_automation.common.ui.page_obejects.base_page import BasePage
from python_automation.common.ui.page_obejects.locators.main_page_locators import SEARCH_FIELD, TITLE, GET_TEXT, GO_BTN, \
    NO_REPO, ERROR_MESSAGE, SUCCESS_MESSAGE
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def wait_for_title_displayed(self):
        self.wait_for_visibility_of_element_located(TITLE)

    def search_user(self, username, enter=None):
        self.type_text(SEARCH_FIELD, username, enter=enter)

    def get_title_text(self):
        element = self.get_element_text(TITLE)
        return element

    def click_go_btn(self):
        self.click_element(GO_BTN)

    def count_results(self):
        count = len(self.driver.find_elements(By.XPATH, "//li"))
        return count

    def get_empty_repo_message(self):
        element = self.get_element_text(NO_REPO)
        return element

    def get_error_user_not_found(self):
        element = self.get_element_text(ERROR_MESSAGE)
        return element

    def get_success_user_message(self):
        element = self.get_element_text(SUCCESS_MESSAGE)
        return element

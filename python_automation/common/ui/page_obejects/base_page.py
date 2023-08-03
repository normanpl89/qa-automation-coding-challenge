import time
from urllib.parse import urlparse
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, selenium_webdriver):
        self.driver = selenium_webdriver

    def quit(self):
        self.driver.quit()

    def wait_for_element_to_be_clickable(self, tuple_selector):
        wait = WebDriverWait(self.driver, 30)
        return wait.until(EC.element_to_be_clickable(tuple_selector))

    def wait_element_exist(self, tuple_selector):
        wait = WebDriverWait(self.driver, 30)
        return wait.until(EC.presence_of_element_located(tuple_selector))

    def wait_for_visibility_of_element_located(self, tuple_selector):
        wait = WebDriverWait(self.driver, 30)
        return wait.until(EC.visibility_of_element_located(tuple_selector))

    def type_text(self, tuple_selector, value=None, tab=None, enter=None):
        element = self.wait_for_visibility_of_element_located(tuple_selector)
        if value:
            for char in value:
                self.wait_for_visibility_of_element_located(tuple_selector).send_keys(char)
                time.sleep(0.1)
        if tab:
            element.send_keys(Keys.TAB)
        if enter:
            element.send_keys(Keys.ENTER)

    def get_element_text(self, tuple_selector):
        element = self.wait_for_visibility_of_element_located(tuple_selector)
        return element.text

    def click_element(self, tuple_selector):
        element = self.wait_for_visibility_of_element_located(tuple_selector)
        element.click()


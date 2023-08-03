from selenium.webdriver.common.by import By

SEARCH_FIELD = (By.ID, "username")
TITLE = (By.XPATH, "//header/h1")
GET_TEXT = (By.XPATH, "//label[@for='username']")
GO_BTN = (By.CSS_SELECTOR, "button.submit")
NO_REPO = (By.CSS_SELECTOR, "p.output-status-text")
ERROR_MESSAGE = (By.CSS_SELECTOR, "p.message-failure")
SUCCESS_MESSAGE = (By.CSS_SELECTOR, "p.message-success")

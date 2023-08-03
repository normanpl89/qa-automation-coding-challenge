import time

import allure
from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from python_automation.tests.ui.constants import APP_URL
from hamcrest import assert_that, equal_to, less_than_or_equal_to
from python_automation.common.ui.page_obejects.main_page import MainPage


@given('I logged on the Application page.')
def step_impl(context):
    service = Service(executable_path='/drivers/chromedriver.exe')
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.get(APP_URL)


@when('I logged I validate the Header of the Page "{header}".')
def step_impl(context, header):
    main_page = MainPage(context.driver)
    main_page.wait_for_title_displayed()
    actual_text = main_page.get_title_text()
    assert_that(actual_text, equal_to(header), 'Verify the header of the page')


@then('I enter a valid user "{user}" and tap enter.')
def step_impl(context, user):
    main_page = MainPage(context.driver)
    main_page.search_user(user, True)
    time.sleep(3)


@then('I enter a valid user "{user}" and click Go.')
def step_impl(context, user):
    main_page = MainPage(context.driver)
    main_page.search_user(user)
    main_page.click_go_btn()
    time.sleep(3)


@then('I validate the result is equal to {expected}.')
def step_impl(context, expected):
    main_page = MainPage(context.driver)
    actual = main_page.count_results()
    assert_that(actual, equal_to(int(expected)), 'Verify list of responses')


@then('I attach an screenshot of the result.')
def step_impl(context, *args, **kwargs):
    allure.attach(context.driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)


@then('I validate the "{message}" message displayed.')
def step_impl(context, message):
    main_page = MainPage(context.driver)
    actual_text = main_page.get_empty_repo_message()
    assert_that(actual_text, equal_to(message), 'Verify the header of the page')


@then('Get the error message "{message}".')
def step_impl(context, message):
    main_page = MainPage(context.driver)
    actual_text = main_page.get_error_user_not_found()
    assert_that(actual_text, equal_to(message), 'Verify the header of the page')


@then('Get the "{message}" message.')
def step_impl(context, message):
    main_page = MainPage(context.driver)
    actual_text = main_page.get_success_user_message()
    assert_that(actual_text, equal_to(message), 'Verify the header of the page')

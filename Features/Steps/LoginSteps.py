from behave import *
from selenium import webdriver
from PageObjectModel.LoginPage import LoginPage
from PageObjectModel.PostLoginPage import PostLoginPage


@given('I navigate to the Login page')
def navigate_to_login(context):
    context.driver = webdriver.Chrome(
        executable_path="C:/Users/hcmartins/Desktop/MachineLearning/PanIntelligenceTests/Drivers/chromedriver.exe")
    context.driver.get("file:///C:/Users/hcmartins/Downloads/index.html")
    context.driver.implicitly_wait(5)
    context.driver.maximize_window()

@when('I enter username "{uname}" and password "{pwd}"')
def enter_username_and_password(context, uname, pwd):
    driver = context.driver
    login = LoginPage(driver)
    login.enter_user_credential(uname, pwd)

@when('I click on the Log-in button')
def step_impl(context):
    driver = context.driver
    driver.login.click_login()

@then('I am taken to the Post-Login Home page')
def step_impl(context):
    driver = context.driver
    # Assuming page title == Home page
    context.assertEqual("Home page", driver.title, "Post-Login page title is not found")

@then('I am successfully logged into the Dashboard page')
def logged_into_the_dashboard_page(context):
    driver = context.driver
    homepage = PostLoginPage(driver)
    text = homepage.driver.capture_page_header()
    assert text == "Welcome to PanIntelligence"

@then('I can close the browser')
def close_browser(context):
    driver = context.driver
    homepage = PostLoginPage(driver)
    homepage.click_logout()
    driver.close()

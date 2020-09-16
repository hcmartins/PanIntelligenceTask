from Locators.Locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_user_credential(self, username, password):
        self.driver.find_element_by_id(Locators.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(username)
        self.driver.find_element_by_id(Locators.password_textbox_id).clear()
        self.driver.find_element_by_id(Locators.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(Locators.login_btn_id).click()




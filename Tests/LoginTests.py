from selenium import webdriver
from PageObjectModel.LoginPage import LoginPage
from PageObjectModel.PostLoginPage import PostLoginPage
import time
import unittest
import HtmlTestRunner

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/hcmartins/Desktop/MachineLearning/PanIntelligenceTests/Drivers/chromedriver.exe")
        #cls.driver = webdriver.chrome()
        cls.driver.get("file:///C:/Users/hcmartins/Downloads/index.html")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid_credentials(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_user_credential("Admin", "admin123")
        login.click_login()

        # Verification
        # Assuming page title == Home page
        self.assertEqual("Home page", driver.title, "Post-Login page title is not found")


    def test_login_invalid_credentials(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_user_credential("InvalidUser", "Password1")
        login.click_login()
        self.assertNotEqual("Home page", driver.title, "Post-Login page title is found")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:/Users/hcmartins/Desktop/MachineLearning/PanIntelligenceTests/Reports'))

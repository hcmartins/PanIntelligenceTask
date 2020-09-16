from Locators.Locators import Locators

class PostLoginPage():
    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        self.driver.find_element_by_linkText(Locators.logout_link_linkText).click()

    def capture_page_header(self):
        self.driver.find_element_by_xpath(Locators.dashboard_header_xpath).text()

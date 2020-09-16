class Locators():

    # Login page objects
    username_textbox_id = "username"
    password_textbox_id = "password"
    #login_btn_id = "btnLogin"
    login_btn_xpath = "button[@type='submit']"

    # Post-login page objects  -  This is an assumption as Post-login pages are not part of this test scope
    logout_link_linkText = "Logout"
    dashboard_header_xpath = "//h1[contains(text(), 'Welcome to PanIntelligence')]"


from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, '[id="login_form"]')
    REGISTRATION_FORM_LINK = (By.CSS_SELECTOR, '[id="register_form"]')
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.does_url_contain('login'), "Login form is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM_LINK), "Login form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD_LINK)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_LINK)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD_LINK)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_LINK)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(password)
        register_button.click()
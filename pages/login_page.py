import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'Login' is not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_address = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_address.send_keys(email)
        password_enter = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_enter.send_keys(password)
        password_confirm = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        password_confirm.send_keys(password)
        time.sleep(2)
        log_in = self.browser.find_element(*LoginPageLocators.LOG_IN)
        log_in.click()


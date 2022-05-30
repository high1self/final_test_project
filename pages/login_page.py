from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # проверка на корректный url адрес
    def should_be_login_url(self):
        login = "login"
        assert login in self.browser.current_url, f"the url is not contains {login}"

    # проверка, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "There is no login form"

    # проверка, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REG), "There is no registration form"

    # регистрация юзера
    def register_new_user(self, email, password):
        enter_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        enter_email.send_keys(email)
        enter_password = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        enter_password.send_keys(password)
        enter_password_repeat = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_REPEAT)
        enter_password_repeat.send_keys(password)
        register_button_click = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        register_button_click.click()



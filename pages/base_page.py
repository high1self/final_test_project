from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import LoginPageLocators



class BasePage():
    # инициализация
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(5)

    # открываем урл
    def open(self):
        self.browser.get(self.url)

    # проверка на видимость элемента
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # проверка на то что элемента нет
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # проверка на то что элемент исчез
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # открываем страницу логина
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # проверяем видимость кнопки логина
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # открываем корзину
    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_OPEN)
        link.click()

    # проверяем что юзер авторизован
    def should_be_authorized_user(self):
        assert self.is_element_present(*LoginPageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"


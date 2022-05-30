from .pages.product_page import ProductPage
import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time


# список страниц по которым проходит тест
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
# добавление товара в корзину гостем
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()  # добавляем в корзину
    product_page.solve_quiz_and_get_code()  # решаем капчу и получаем ответ
    product_page.compare_prices()  # сравнение цен в корзине и в карточке продукта
    product_page.compare_product_name()  # сравнение названия продукта в карточке товара и корзине


@pytest.mark.xfail
# негативная проверка на видимость сообщения об успешном добавлении в корзину
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    product_page.should_not_be_success_message()

# позитивная проверка на видимость сообщения об успешном добавлении в корзину
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()


@pytest.mark.xfail
# негативная проверка на исчезновение сообщения об успешном добавлении в корзину
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    product_page.should_be_success_message_is_disappeared()

# проверка на видимость кнопки логина/регистрации
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
# проверяем возможность зайти на страницу логина из страницы продукта
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
# проверяем что корзина пустая у гостя
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.check_busket_is_empty() # проверяем что в корзине нет товара
    page.check_text_in_busket_is_empty() # проверяем что нет блока про сумму корзины


@pytest.mark.login
# добавление товара под аккаунтом юзера
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True) # запускать перед каждой функцией, без явного вызова
    # тестовые данные для входа в аккаунт + вход в аккаунт
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "register_new_user"
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = LoginPage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.go_to_login_page()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    # проверяем что корзина пуста под юзером
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    # проверяем что юзер может добавлять товар в корзину
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.add_to_basket()
        product_page.compare_prices() # сравниваем цены продукта в корзине и в карточке
        product_page.compare_product_name() # сравниваем название продукта в корзине и в карточке

from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Проверяем что в корзине нет товаров
    def check_busket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_HAVE_PRODUCTS), "Busket is not empty"

    # Проверяем что есть текст о том что в корзине нет товаров
    def check_text_in_busket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TEXT_IS_EMPTY), "There is no text about empty busket"

from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException # в начале файла



class ProductPage(BasePage):

    def add_to_basket(self):
        # открываем страницу
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BUTTON)
        link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def compare_prices(self):
        busket_price = self.browser.find_element(*ProductPageLocators.BUSKET_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert busket_price == product_price, "Prices dont equal"

    def compare_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BUSKET).text
        assert product_name == product_name_in_basket, "Names dont equal"

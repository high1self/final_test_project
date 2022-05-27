from selenium.webdriver.common.by import By


class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REG = (By.CSS_SELECTOR, "#register_form")

    LOGIN_EMAIL = (By.XPATH, "//input[@name='login-username']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@name='login-password']")
    BUTTON_LOGIN = (By.XPATH, "//button[@name='login_submit']")

    REG_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    REG_PASSWORD = (By.XPATH, "//input[@name='registration-password1']")
    REG_PASSWORD_REPEAT = (By.XPATH, "//input[@name='registration-password2']")
    BUTTON_REG = (By.XPATH, "//button[@name='registration_submit']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class ProductPageLocators():
    ADD_TO_BUSKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_IN_BUSKET = (By.CSS_SELECTOR, "#messages>:nth-child(1) .alertinner>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    BUSKET_PRICE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in>.alertinner>p>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main>.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>:nth-child(1) .alertinner>strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUSKET_OPEN = (By.CSS_SELECTOR, ".btn-group .btn.btn-default:nth-child(1)")

class BasketPageLocators():
    BASKET_HAVE_PRODUCTS = (By.CSS_SELECTOR, "#basket_totals")
    BASKET_TEXT_IS_EMPTY = (By.XPATH, "//div[@id='content_inner']/p")

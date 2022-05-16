from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

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
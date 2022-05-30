import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# добавление опций
def pytest_addoption(parser):
    # параметр - выбор браузера
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome only")
    # параметр - выбор языка
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")


@pytest.fixture(scope="function")
# описываем экземпляр браузера
def browser(request):
    try:
        browser_name = request.config.getoption("browser_name")
        user_language = request.config.getoption("language")
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
        yield browser
        print("\nquit browser..")
    finally:
        browser.quit()

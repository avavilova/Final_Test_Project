import pytest
from pages import MainPage
from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from const import BASE_URL, BROWSER, BROWSER_NAME, HEADLESS, HEADLESS_OPTION


def get_browser_class():
    if BROWSER == BROWSER_NAME.CHROME:
        return Chrome, ChromeService, ChromeDriverManager, ChromeOptions, HEADLESS_OPTION.CHROME_HEADLESS
    if BROWSER == BROWSER_NAME.FIREFOX:
        return Firefox, FirefoxService, GeckoDriverManager, FirefoxOptions, HEADLESS_OPTION.FIREFOX_HEADLESS
    raise Exception(f'Invalid browser name={BROWSER}')


def create_driver():
    webdriver_class, service_class, manager_class, options_class, headless_class = get_browser_class()
    manager = manager_class()
    service = service_class(manager.install())
    options = options_class()
    if HEADLESS:
        options.add_argument(headless_class)
    driver = webdriver_class(options=options, service=service)
    driver.implicitly_wait(1)
    return driver


@pytest.fixture(scope='session')
def driver():
    driver_ = create_driver()
    yield driver_
    driver_.close()


@pytest.fixture(scope='session')
def kinopoisk_main_page(driver):
    main_page = MainPage(driver, BASE_URL)
    return main_page

from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CLASS_NAME, "styles_loginButton__LWZQp")

class LoginPageLocators():
    EMAIL_INPUT = (By.ID, "passp-field-login")
    LOGIN_BUTTON = (By.ID, "passp:sign-in")
    LOGIN_FORM = (By.CSS_SELECTOR, ".passp-auth-content")
    ERROR_MSG = (By.ID, "field:input-login:hint")

class MainPageLocators():
    SEARCH_INPUT = (By.XPATH, "//input[@name='kp_query']")
    SEARCH_SUGGESTED_ITEM = (By.CSS_SELECTOR, "article.styles_root__MtNP0.kinopoisk-header-suggest-item")
    SEARCH_PAGE_LINK = (By.XPATH, "//a[@href='/s/' and @aria-label='Расширенный поиск']")
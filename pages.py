from __future__ import annotations

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from const import TIMEOUTS
from locators import *


class BasePage:
    TITLE = None

    def __init__(self, driver: Chrome, url: str):
        self.driver = driver
        self.url = url

    def go_to_site(self, timeout=TIMEOUTS.GET_URL):
        self.driver.get(self.url)
        condition = EC.title_is(self.TITLE)
        return WebDriverWait(self.driver, timeout).until(condition)

    def find_element(self, locator: tuple[any, str], timeout=TIMEOUTS.FIND_ELEMENT) -> WebElement:
        condition = EC.presence_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until(condition)

    def find_elements(self, locator: tuple[any, str], timeout=TIMEOUTS.FIND_ELEMENT) -> list[WebElement]:
        condition = EC.presence_of_all_elements_located(locator)
        return WebDriverWait(self.driver, timeout).until(condition)

    def is_exists(self, locator: tuple[any, str]):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def is_not_exists(self, locator: tuple[any, str], timeout=TIMEOUTS.FIND_ELEMENT):
        condition = EC.presence_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until_not(condition)

    def click_to(self, locator: tuple[any, str], timeout=TIMEOUTS.FIND_ELEMENT):
        element = self.find_element(locator, timeout)
        element.click()
        return element


class MainPage(BasePage):
    TITLE = 'Кинопоиск. Все фильмы планеты.'

    def go_to_search(self):
        self.click_to(MainPageLocators.SEARCH_PAGE_LINK)
        return SearchPage(self.driver, self.driver.current_url)

    def get_default_suggested_search_results(self) -> list[WebElement]:
        self.click_to(MainPageLocators.SEARCH_INPUT)
        suggested_search_results_locator = (By.CSS_SELECTOR, "a.styles_mainLink__A4Xkh")
        return self.find_elements(suggested_search_results_locator)

    def is_default_suggested_search_top10_label_exist(self) -> bool:
        self.click_to(MainPageLocators.SEARCH_INPUT)
        suggested_top10_label_locator = (
            By.CSS_SELECTOR, "h3.styles_title__irLOv.kinopoisk-header-suggest-group__title")
        return self.is_exists(suggested_top10_label_locator)

    def get_search_results(self, request_string: str) -> list[WebElement]:
        search_input = self.click_to(MainPageLocators.SEARCH_INPUT)
        search_input.send_keys(request_string)
        search_results_locator = (By.CSS_SELECTOR, "article.styles_root__MtNP0.kinopoisk-header-suggest-item")
        return self.find_elements(search_results_locator)

    def get_suggested_items_headers_searched(self) -> list[str]:
        headers = self.find_elements((By.CSS_SELECTOR, "h4.styles_title__7ZVXS.kinopoisk-header-suggest-item__title"))
        return [header.text for header in headers]


class SearchPage(BasePage):
    TITLE = 'Кинопоиск — Все фильмы планеты'

    def get_country_search_options(self) -> list[WebElement]:
        return self.find_elements((By.XPATH, '//select[@id="country"]/option'))

    def get_countries(self) -> tuple[str]:
        return tuple([option.text for option in self.get_country_search_options()])

    def set_country(self, country_name):
        self.click_to((By.XPATH, '//select[@id="country"]'))
        self.click_to((By.XPATH, f'//select[@id="country"]/option[text()="{country_name}"]'))

    def get_current_country_text(self) -> str:
        for option in self.get_country_search_options():
            if option.is_selected():
                return option.text
        else:
            raise Exception('No options selected in country dropdown')

    def get_genre_options(self) -> list[WebElement]:
        return self.find_elements((By.XPATH, '//select[@id="m_act[genre]"]/option'))

    def get_genres(self) -> tuple[str]:
        return tuple([option.text for option in self.get_genre_options()])

    def set_genre(self, genre_name):
        genre_select = Select(self.find_element((By.XPATH, '//select[@id="m_act[genre]"]')))
        genre_select.select_by_visible_text(genre_name)

    def get_current_genre_text(self) -> str:
        for option in self.get_genre_options():
            if option.is_selected():
                return option.text
        else:
            raise Exception('No options selected in genre dropdown')
        

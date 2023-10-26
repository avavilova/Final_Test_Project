import allure
import pytest

from pages import *


@pytest.fixture(scope='module')
def search_page(kinopoisk_main_page):
    kinopoisk_main_page: MainPage
    kinopoisk_main_page.go_to_site()
    kinopoisk_search_page: SearchPage = kinopoisk_main_page.go_to_search()
    yield kinopoisk_search_page
    kinopoisk_main_page.go_to_site()

@allure.story("Search page")
@allure.testcase("Country dropdown")
def test_is_country_selected(search_page):
    search_page: SearchPage
    country_selected = "Беларусь"
    search_page.set_country(country_selected)
    assert search_page.get_current_country_text() == country_selected

@allure.story("Search page")
@allure.testcase("Genre dropdown")
def test_is_genre_selected(search_page):
    search_page: SearchPage
    genre_selected = "биография"
    search_page.set_genre(genre_selected)
    assert search_page.get_current_genre_text() == genre_selected


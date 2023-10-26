import os

BASE_URL = 'https://www.kinopoisk.ru/'


class TIMEOUTS:
    GET_URL = 120
    FIND_ELEMENT = 20


BROWSER = os.getenv('BROWSER', 'chrome')
HEADLESS = os.getenv('HEADLESS', False)


class HEADLESS_OPTION:
    CHROME_HEADLESS = '--headless=new'
    FIREFOX_HEADLESS = '--headless'


class BROWSER_NAME:
    CHROME = 'chrome'
    FIREFOX = 'firefox'
    ALL = (CHROME, FIREFOX)


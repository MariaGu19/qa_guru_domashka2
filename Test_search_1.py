import pytest
from selene import browser, be, have


@pytest.fixture()
def open_browser():
    """Размеры браузера при запуске"""
    browser.driver.set_window_size(1896, 1080)
    browser.open('https://google.com')
    yield browser


def test_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_nothing_found(open_browser):
    browser.element('[name="q"]').should(be.blank).type('fjjkfsjfjebfebrghefkjwjwe').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))

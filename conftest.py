from selene.support.shared import browser
import pytest


@pytest.fixture(scope='session', autouse=True)
def browser_settings():
    browser.config.browser_name = "chrome"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield

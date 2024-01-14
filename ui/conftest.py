import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub", options=options)
    browser.config.driver = driver
    browser.config.timeout = 10.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://www.tinkoff.ru/')

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

import pytest

from selene.support.shared import browser


@pytest.fixture(params=[(3840, 2160), (1920, 1080)])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(1024, 768), (800, 600)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(3840, 2160), (1920, 1080), (1024, 768), (800, 600)])
def is_desktop_browser(request):
    resolution = request.param
    if resolution in [(3840, 2160), (1920, 1080)]:
        width, height = resolution
        browser.config.window_width = width
        browser.config.window_height = height

        return True
    else:
        return False


@pytest.fixture(params=[(3840, 2160), (1920, 1080), (1024, 768), (800, 600)])
def is_mobile_browser(request):
    resolution = request.param
    if resolution in [(1024, 768), (800, 600)]:
        width, height = resolution
        browser.config.window_width = width
        browser.config.window_height = height

        return True
    else:
        return False

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from utils import attach
@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub", options=options)
    browser.config.base_url = "https://demoqa.com"
    browser.config.driver = driver
    browser.config.timeout = 6.0
    browser.config.window_width = 412
    browser.config.window_height = 914

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from utils import attach


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub", options=options)
    browser.config.base_url = "https://demoqa.com"
    browser.config.driver = driver
    browser.config.timeout = 6.0
    browser.config.window_width = 412
    browser.config.window_height = 914

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
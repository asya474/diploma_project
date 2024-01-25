import pytest
from selene import browser
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from helper.attach_helpers import add_screenshot, add_logs, add_html, add_video


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
    browser.config.window_width = 333
    browser.config.window_height = 628

    yield browser

    add_screenshot(browser)
    add_logs(browser)
    add_html(browser)
    add_video(browser)

    browser.quit()

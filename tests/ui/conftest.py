from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from selene.support.shared import browser
from tests.ui.utils import attach


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
    browser.config.window_width = 412
    browser.config.window_height = 914

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
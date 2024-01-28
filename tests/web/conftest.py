import sys

sys.path.insert(0, '../helper/attach_helpers.py')
import pytest
from helper_for_test import attach_helpers
from selene import browser
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




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

    attach_helpers.add_screenshot(browser)
    attach_helpers.add_logs(browser)
    attach_helpers.add_html(browser)
    attach_helpers.add_video(browser)

    browser.quit()

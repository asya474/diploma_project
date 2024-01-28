import json

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
# from selene import browser
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import Settings
from helper import attach_helpers, get_env_path
from helper.attach_helpers import add_screenshot, add_logs, add_html, add_video


@pytest.fixture(scope="function")
def browser_setup():
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
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    add_screenshot(browser)
    add_logs(browser)
    add_html(browser)
    add_video(browser)

    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--env',
        help='Environment for test',
        choices=['browserstack', 'local'],
        default='browserstack'
    )


@pytest.fixture(scope='function')
def set_mobile_browser(request):
    environment = request.config.getoption('--env')

    load_dotenv(get_env_path.get_mobile_env_path(environment))
    settings = Settings()
    options = UiAutomator2Options()

    if environment == 'browserstack':
        options.load_capabilities({
            "platformName": settings.platformName,
            "platformVersion": settings.platformVersion,
            "deviceName": settings.deviceName,

            # Set URL of the application under test
            "app": settings.app,

            # Set other BrowserStack capabilities
            'bstack:options': {
                "projectName": settings.projectName,
                "buildName": settings.buildName,
                "sessionName": settings.sessionName,
                'networkLogs': settings.networkLogs,

                # Set your access credentials
                "userName": settings.userName,
                "accessKey": settings.accessKey
            }
        })

    elif environment == 'local':
        options.load_capabilities({
            'appium:automationName': settings.automationName,
            'appium:app': get_env_path.get_app_path(settings.app),
            'platformName': settings.platformName,
            'appium:appWaitActivity': settings.appWaitActivity
        })

    browser.config.driver = webdriver.Remote(settings.remoteBrowser, options=options)

    yield environment

    if environment == 'browserstack':
        session_id = browser.execute_script('browserstack_executor: {"action": "getSessionDetails"}')
        video_url = json.loads(session_id)['video_url']
        attach_helpers.mobile_attach_video(video_url)

    browser.quit()


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

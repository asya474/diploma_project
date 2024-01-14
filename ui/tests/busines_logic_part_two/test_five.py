@pytest.mark.desktop
def test_github_sign_in_desktop(is_desktop_browser):
    if not is_desktop_browser:
        pytest.skip(reason='Тест для десктопного разрешения экрана')
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.mobile
def test_github_sign_in_mobile(is_mobile_browser):
    if not is_mobile_browser:
        pytest.skip(reason='Тест для мобильного разрешения экрана')
    browser.open('https://github.com')
    browser.element('.js-details-target.Button--link').should(be.clickable).click()
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))

import pytest
from selene import browser, be, have


@pytest.mark.desktop
@pytest.mark.parametrize("desktop_browser", [(3840, 2160), (1920, 1080)], indirect=True)
def test_github_sign_in_desktop(desktop_browser):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.mobile
@pytest.mark.parametrize("mobile_browser", [(1024, 768), (800, 600)], indirect=True)
def test_github_sign_in_mobile(mobile_browser):
    browser.open('https://github.com')
    browser.element('.js-details-target.Button--link').should(be.clickable).click()
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))

import pytest
from selene import browser, be, have


@pytest.mark.desktop
def test_github_sign_in_desktop(desktop_browser):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.mobile
def test_github_sign_in_mobile(mobile_browser):
    browser.open('https://github.com')
    browser.element('.js-details-target.Button--link').should(be.clickable).click()
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))
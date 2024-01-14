import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "e.goldinova")
@allure.description("Test without allure steps and decorators")
@allure.feature("Search issue on github")
@allure.link('https://github.com', name='Testing')
def test_find_issue_on_github():
    browser.open('https://github.com')

    s(".header-search-button").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible)

    browser.quit()
import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "e.goldinova")
@allure.description("Test with allure steps")
@allure.feature("Search issue on github")
@allure.link('https://github.com', name='Testing')
def test_find_issue_on_github_with_decorators():
    open_main_page()
    find_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    go_to_issue_tab()
    check_issue()
    browser.quit()


@allure.step("Open main page")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Find repository {repo}")
def find_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").submit()


@allure.step("Go to repository {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Go to Issues tab")
def go_to_issue_tab():
    s("#issues-tab").click()


@allure.step("Check issue #76")
def check_issue():
    s(by.partial_text("#76")).should(be.visible)

import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "e.goldinova")
@allure.description("Test with allure steps")
@allure.feature("Search issue on github")
@allure.link('https://github.com', name='Testing')
def test_find_issue_on_github_with_steps():
    with allure.step("Open main page"):
        browser.open("https://github.com")

    with allure.step("Find repository"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("Go to repository"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Go to Issues tab"):
        s("#issues-tab").click()

    with allure.step("Check issue #76"):
        s(by.partial_text("#76")).should(be.visible)

    browser.quit()
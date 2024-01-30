from allure_commons._allure import step
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search_wiki(android_mobile_management):
    with allure.step('Open second page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Open third page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Open fourth page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Accept User Agreement'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')).click()

    with step('Type search'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_container")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Appium")

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        results.should(have.size_greater_than(0))
        results.first.should(have.text("Appium"))


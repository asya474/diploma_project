import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_open_some_article(android_mobile_management):
    with allure.step('Verify content page 1'):
        results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
        results.should(have.exact_text("The Free Encyclopedia\n…in over 300 languages"))

    with allure.step('Open next page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Verify content page 2'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).wait_until(be.visible)
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('New ways to explore'))

    with allure.step('Open next page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Verify content page 3'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).wait_until(be.visible)
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Reading lists with sync'))

    with allure.step('Press Continue button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Verify content page 4'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).wait_until(be.visible)
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Send anonymous data'))

    with allure.step('Accept User Agreement'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')).click()

    with step('Open wiki and search the article'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_container")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Japan")
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).click()

    with step('Verify article found'):
        browser.element((AppiumBy.XPATH,
                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[1]")).should(
            have.text("Japan"))
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

def test_open_some_article(set_mobile_browser):
    with step('Press Skip button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with step('Open wiki and search the article'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_container")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Japan')
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).click()

    with step('Verify article found'):
        browser.element((AppiumBy.XPATH,
                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[1]")).should(
            have.text('Japan'))
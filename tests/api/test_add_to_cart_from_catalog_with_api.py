from allure_commons._allure import step
from selene import browser, have

from helper.api_helpers.utils import demowebshop_api_post


def test_add_to_cart_from_catalog_with_api(browser_setup):
    response = demowebshop_api_post('/addproducttocart/catalog/22/1/1')
    cookie = response.cookies.get("Nop.customer")

    with step("Set cookie from API"):
        browser.open('/')

        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})

    with step("Open cart"):
        browser.open('/cart')

    with step("Check one item presents"):
        browser.all('.cart-item-row').should(have.size(1))
        (browser.all('.cart-item-row').element_by(have.text('Health Book'))
         .element('[name^="itemquantity"]').should(have.value("1")))

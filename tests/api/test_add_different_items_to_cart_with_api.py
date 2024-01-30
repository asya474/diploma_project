from allure_commons._allure import step
from selene import have
from selene.support.shared import browser

from helper.api_helpers.utils import demowebshop_api_post


def test_add_different_items_to_cart_with_api(api_browser):
    browser.config.base_url = 'https://demowebshop.tricentis.com'
    response = demowebshop_api_post('/addproducttocart/details/28/1',
                                    data={"product_attribute_28_7_10": 25,
                                          "product_attribute_28_1_11": 31,
                                          "addtocart_28.EnteredQuantity": 4})
    cookie = response.cookies.get("Nop.customer")
    demowebshop_api_post('/addproducttocart/details/45/1',
                         data={"addtocart_45.EnteredQuantity": 1},
                         cookies={"Nop.customer": cookie})

    with step("Set cookie from API"):
        browser.open('/')
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})

    with step("Open cart"):
        browser.open('/cart')

    with step("Check two items present"):
        browser.all('.cart-item-row').should(have.size(2))
        (browser.all('.cart-item-row').element_by(have.text('Fiction'))
         .element('[name^="itemquantity"]').should(have.value("1")))
        (browser.all('.cart-item-row').element_by(have.text('Blue and green Sneaker'))
         .element('[name^="itemquantity"]').should(have.value("4")))
    with step("Check total"):
        browser.element('.order-total').should(have.exact_text("68.00"))

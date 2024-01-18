from api.utils import demowebshop_api_post


def test_add_4_items_to_cart_with_api():
    browser.config.base_url = 'https://demowebshop.tricentis.com'
    response = demowebshop_api_post('/addproducttocart/details/45/1', data={"addtocart_45.EnteredQuantity": 4})
    cookie = response.cookies.get("Nop.customer")

    with step("Set cookie from API"):
        browser.open('/')
        browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})

    with step("Open cart"):
        browser.open('/cart')

    with step("Check four items present"):
        browser.all('.cart-item-row').should(have.size(1))
        (browser.all('.cart-item-row').element_by(have.text('Fiction'))
         .element('[name^="itemquantity"]').should(have.value("4")))
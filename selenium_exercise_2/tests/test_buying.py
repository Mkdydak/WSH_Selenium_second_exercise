from pages.home import HomePage
from pages.products import ProductsPage
from pages.cart_summary import CartSummary

def test_buying(driver):
    home_page = HomePage(driver)
    home_page.search_product("dresses")
    product_page = ProductsPage(driver)
    product_page.add_element_to_cart()
    product_page.proceed_to_checkout()
    cart_summary = CartSummary(driver)
    cart_summary.price_smaller_than_50()
    cart_summary.total_shipping_2_dollars()








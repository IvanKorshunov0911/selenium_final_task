import time
from .pages.product_page import ProductPage

def test_guest_can_add_good_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_added_to_cart_message()
    page.should_be_cart_price_message()

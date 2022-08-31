from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_LINK)
        add_to_cart_link.click()

    def should_be_added_to_cart_message(self):
        title = self.get_element_text(*ProductPageLocators.PRODUCT_NAME).strip()
        cart_message = self.get_element_text(*ProductPageLocators.ADDED_TO_CART_MESSAGE).strip()
        print(title)
        print(cart_message)
        assert cart_message == title, f'Expected "{cart_message}" equal "{title}"'

    def should_be_cart_price_message(self):
        price = self.get_element_text(*ProductPageLocators.PRICE).strip()
        cart_price_message = self.get_element_text(*ProductPageLocators.CART_PRICE_MESSAGE).strip()
        print(price)
        print(cart_price_message)
        assert cart_price_message == price, f'Expected "{cart_price_message}" equal "{price}"'

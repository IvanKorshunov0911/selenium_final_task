from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty(self):
        message = self.get_element_text(*CartPageLocators.EMPTY_CART_LINK).strip()
        assert 'Your basket is empty.' in message, "Login form is not presented"
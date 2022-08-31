from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, '[id="login_form"]')
    REGISTRATION_FORM_LINK = (By.CSS_SELECTOR, '[id="register_form"]')

class ProductPageLocators():
    ADD_TO_CART_LINK = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"] > h1')
    PRICE = (By.CSS_SELECTOR, '[class="price_color"]')
    CART_PRICE_MESSAGE = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1)')

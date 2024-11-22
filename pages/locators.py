from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    pass

class ProductPageLocators():
    ADD_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    ADDED_TEXT = (By.CLASS_NAME, "alertinner")
from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.NAME, "registration-email")
    PASSWORD = (By.NAME, "registration-password1")
    PASSWORD_CONFIRM = (By.NAME, "registration-password2")
    LOG_IN = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, "div.product_main h1")
    ADD_BOOK = (By.CSS_SELECTOR, "div.alertinner strong")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, "div.alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    GO_BASKET = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class Basket():
    BASKET_CLEAR = (By.CSS_SELECTOR, "basket-items")
    BASKET_CLEAR_TEXT = (By.CSS_SELECTOR, "#content_inner")


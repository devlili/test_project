from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def go_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        basket.click()
        self.solve_quiz_and_get_code()

    def book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        a = book_name.text
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.ADD_BOOK)
        b = book_name_in_basket.text
        print(a,b)
        assert a == b, 'Название товара не совпадает'

    def price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        a = price.text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET)
        b = price_in_basket.text
        print(a, b)
        assert a == b, 'Цена товара не совпадает'

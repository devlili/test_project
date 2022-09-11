from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        basket.click()
        if "promo=offer" in self.browser.current_url:
            self.solve_quiz_and_get_code()

    def book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        book_name = book_name.text
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.ADD_BOOK)
        book_name_in_basket = book_name_in_basket.text
        print(book_name, book_name_in_basket)
        assert book_name == book_name_in_basket, 'Book name is not th same in basket'

    def price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        price = price.text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET)
        price_in_basket = price_in_basket.text
        print(price, price_in_basket)
        assert price == price_in_basket, 'Price is not the same in basket'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"



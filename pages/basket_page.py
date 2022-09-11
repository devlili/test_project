from .base_page import BasePage
from .locators import Basket

class BasketPage(BasePage):
    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*Basket.BASKET_CLEAR), \
            "Goods are in the basket"

    def basket_is_empty_message(self):
        assert self.is_element_present(*Basket.BASKET_CLEAR_TEXT), "Basket is not empty"
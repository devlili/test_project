import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param ("7", marks=pytest.mark.xfail(reason="some bug")), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.book_name()
    page.price()
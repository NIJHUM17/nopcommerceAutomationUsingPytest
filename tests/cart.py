import ast

import pytest

from object.openBrowser import OpenBrowser
from object.reg import Register
from data_rd import Data
from object.login import Login
from object.search import Search
from object.cart import Cart
from object.checkout import CheckOut


class Test_4:
#cart
    test_data = Data()
    testData = test_data.data()
    log = ast.literal_eval(testData['TEST_DATA']['login_data'])
    search = ast.literal_eval(testData['TEST_DATA']['search_data'])

    @pytest.mark.order(4)
    def test_shop(self, driver, config, locator):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        search = Search(driver, locator)
        shoppingcart = Cart(driver, locator)
        open_url.open_webBrowser()
        login.log_in(self.log)
        search.search_box(self.search)
        shoppingcart.shopping_cart()
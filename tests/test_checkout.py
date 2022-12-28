import pytest
import ast
from object.login import Login
from object.checkout import CheckOut
from object.openBrowser import OpenBrowser
from data_reader import Data
from object.search import Search
from object.shoppingCart import ShoppingCart


class Test_5_checkout:
    testData = Data().data()
    log = ast.literal_eval(testData['DATA']['login_data'])
    search = ast.literal_eval(testData['DATA']['search_data'])
    checkOut = ast.literal_eval(testData['DATA']['checkout_data'])

    @pytest.mark.order(5)
    def test_checkout(self, driver, config, locator):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        search = Search(driver, locator)
        shop_cart = ShoppingCart(driver, locator)
        check_out = CheckOut(driver, locator)
        open_url.open_webBrowser()
        login.login_(self.log)
        search.searching(self.search)
        shop_cart.shopping_cart()
        check_out.checkout_(self.checkOut)

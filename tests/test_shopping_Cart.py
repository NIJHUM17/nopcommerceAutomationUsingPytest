import pytest
import ast
from object.login import Login
from object.search import Search
from object.shoppingCart import ShoppingCart
from object.openBrowser import OpenBrowser
from data_reader import Data


class Test_4_shoppingCart:
    testData = Data().data()
    log = ast.literal_eval(testData['DATA']['login_data'])
    search = ast.literal_eval(testData['DATA']['search_data'])

    @pytest.mark.order(4)
    def test_shop(self, driver, config, locator):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        search = Search(driver, locator)
        shop_cart = ShoppingCart(driver, locator)
        open_url.open_webBrowser()
        login.login_(self.log)
        search.searching(self.search)
        shop_cart.shopping_cart()

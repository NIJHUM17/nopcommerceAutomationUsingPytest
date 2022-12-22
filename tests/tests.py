import ast

import pytest

from object.openBrowser import OpenBrowser
from object.reg import Register
from data_rd import Data
from object.login import Login
from object.search import Search
from object.cart import Cart
from object.checkout import CheckOut




class Test_1:
#registration
    td = Data()
    testdata = td.data()
    reg = ast.literal_eval(testdata['DATA']['registration_data'])

    @pytest.mark.order(1)
    def test_registration(self, driver, config, locator):
        open_url = OpenBrowser(driver, config)
        register = Register(driver, locator)
        open_url.open_webBrowser()
        register.registration(self.reg)




class Test_2:
#login
    td = Data()
    testData = td.data()
    log = ast.literal_eval(testData['DATA']['login_data'])

    @pytest.mark.order(2)
    def test_login(self, driver, config, locator):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        open_url.open_webBrowser()
        login.log_in(self.log)




class Test_3:
#search
    td = Data()
    testData = td.data()
    log = ast.literal_eval(testData['DATA']['login_data'])
    search = ast.literal_eval(testData['DATA']['search_data'])

    @pytest.mark.order(3)
    def test_search(self, driver, config, locator):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        search = Search(driver, locator)
        open_url.open_webBrowser()
        login.log_in(self.log)
        search.search_box(self.search)





class Test_4:
#cart
    td = Data()
    testData = td.data()
    log = ast.literal_eval(testData['DATA']['login_data'])
    search = ast.literal_eval(testData['DATA']['search_data'])

    @pytest.mark.order(4)
    def test_shop(self, driver, config, locator):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        search = Search(driver, locator)
        shop_cart = Cart(driver, locator)
        open_url.open_webBrowser()
        login.log_in(self.log)
        search.search_box(self.search)
        shop_cart.shopping_cart()




class Test_5:
#checkout
    td = Data()
    testData = td.data()
    log = ast.literal_eval(testData['DATA']['login_data'])
    checkOut = ast.literal_eval(testData['DATA']['checkOut_data'])

    @pytest.mark.order(5)
    def test_checkout(self, driver, config, locator):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        check_out = CheckOut(driver, locator)
        open_url.open_webBrowser()
        login.log_in(self.log)
        check_out.checkout_billing_details(self.checkOut)

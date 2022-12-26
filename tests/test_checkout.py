import ast

import pytest

from object.openBrowser import OpenBrowser
from object.reg import Register
from data_rd import Data
from object.login import Login
from object.search import Search
from object.cart import Cart
from object.checkout import CheckOut


class Test_5:
#checkout
    test_data = Data()
    testData = test_data.data()
    log = ast.literal_eval(testData['TEST_DATA']['login_data'])
    checkOut = ast.literal_eval(testData['TEST_DATA']['checkOut_data'])

    @pytest.mark.order(5)
    def test_checkout(self, driver, config, locator):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        check_out = CheckOut(driver, locator)
        open_url.open_webBrowser()
        login.log_in(self.log)
        check_out.checkout_billing_details(self.checkOut)
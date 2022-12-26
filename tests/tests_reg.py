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
    reg = ast.literal_eval(testdata['TEST_DATA']['registration_data'])

    @pytest.mark.order(1)
    def test_registration(self, driver, config, locator):
        open_url = OpenBrowser(driver, config)
        register = Register(driver, locator)
        open_url.open_webBrowser()
        register.registration(self.reg)










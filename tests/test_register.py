import ast

import pytest

from object.openBrowser import OpenBrowser
from object.register import Register
from datareader import Data


class Test_1_Register:
    testdata = Data().data()
    reg = ast.literal_eval(testdata['DATA']['registration_data'])

    @pytest.mark.order(1)
    def test_registration(self, driver, config, locator):
        open_url = OpenBrowser(driver, config)
        register = Register(driver, locator)
        open_url.open_webBrowser()
        register.registration(self.reg)

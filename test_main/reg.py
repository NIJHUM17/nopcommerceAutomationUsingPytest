

import ast

import pytest

from objects.open_browser import OpenBrowser
from objects.registration import Registration



class Test_001_register:
    td = Data()
    testdata = td.data()
    reg = ast.literal_eval(testdata['DATA']['registration_data'])

    @pytest.mark.order(1)
    def test_registration(self, driver, config, locator, email):
        open_url = OpenBrowser(driver, config)
        register = Registration(driver, locator)
        open_url.open_webBrowser()
        register.registration(email, self.reg)
        assert register.x == "nopCommerce demo store. Register"
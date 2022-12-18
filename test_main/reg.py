

import ast
import time
import pytest

from objects.open_browser import OpenBrowser
from objects.registration import Registration



class Test_1:
    td = Data()
    testdata = td.data()
    reg = ast.literal_eval(testdata['DATA']['registration_data'])

    @pytest.mark.order(1)
    def test_registration(self, driver, config):
        open_url = OpenBrowser(driver, config)
        
        open_url.open_webBrowser()

import pytest
import ast

from object.login import Login
from object.openBrowser import OpenBrowser
from data_reader import Data


class Test_2_Login:
    testData = Data().data()
    log = ast.literal_eval(testData['DATA']['login_data'])

    @pytest.mark.order(2)
    def test_login(self, driver, config, locator):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        open_url.open_webBrowser()
        login.log_in(self.log)

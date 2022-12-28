import pytest
import ast
from object.search import Search
from object.login import Login
from object.openBrowser import OpenBrowser
from data_reader import Data


class Test_3_search:
    testData = Data().data()
    log = ast.literal_eval(testData['DATA']['login_data'])
    search = ast.literal_eval(testData['DATA']['search_data'])

    @pytest.mark.order(3)
    def test_search(self, driver, config, locator):
        open_url = OpenBrowser(driver, config)
        login = Login(driver, locator)
        search = Search(driver, locator)
        open_url.open_webBrowser()
        login.login_(self.log)
        search.searching(self.search)

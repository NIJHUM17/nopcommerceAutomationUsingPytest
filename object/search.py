
import time
class Search:

    def __init__(self, driver, locator):

        self.driver = driver
        time.sleep(3)
        self.searching = locator["LOCATORS"]["searching"]
        self.search_product = locator["LOCATORS"]["search_product"]
        self.search_inside = locator["LOCATORS"]["search_inside"]

    def search_box(self, search):
        time.sleep(3)
        self.driver.find_element("xpath", self.searching).click()

        self.driver.find_element("id", self.search_product).send_keys(search.searchData.productName)
        time.sleep(1)
        self.driver.find_element("xpath", self.search_inside).click()








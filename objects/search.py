import time
import locators
import test_data.search_data

class Search:

    def __init__(self, driver):
        self.driver = driver

    def searching(self):
        time.sleep(3)
        self.driver.find_element("xpath", locators.searching).click()
        time.sleep(3)

    def searchproduct(self):
        self.driver.find_element("id",locators.search_product).send_keys(test_data.search_data.productName)
        time.sleep(1)

    def searchinside(self):
        self.driver.find_element("xpath", locators.search_inside).click()
        time.sleep(3)
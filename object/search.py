import time


class Search:
    def __init__(self, driver, locator):
        self.driver = driver
        self.search = locator["LOCATORS"]["search"]
        self.search_click = locator["LOCATORS"]["search_click"]
        self.product = locator["LOCATORS"]["product"]

    def searching(self, search):
        self.driver.find_element("id", self.search).click()
        self.driver.find_element("id", self.search).send_keys(search['productName'])
        time.sleep(2)
        self.driver.find_element("xpath", self.search_click).click()
        self.driver.find_element("xpath", self.product).click()
        time.sleep(3)

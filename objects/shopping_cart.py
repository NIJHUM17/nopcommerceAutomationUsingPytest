import time
import locators


class Shopping_cart:

    def __init__(self, driver):
        self.driver = driver

    def add_cart(self):
        time.sleep(4)
        self.driver.find_element("xpath", locators.add_cart).click()
        time.sleep(1)

    def Shop_cart(self):
        time.sleep(3)
        self.driver.find_element("xpath", locators.shopping_cart).click()
        time.sleep(1)
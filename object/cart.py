import time
class Cart:
    def __init__(self, driver, locator):
        self.shopCart = None
        self.driver = driver
        self.add_cart = locator["LOCATORS"]["add_cart"]
        self.shopping_cart = locator["LOCATORS"]["shopping_cart"]

    def shopping_cart(self):

        self.driver.find_element("id", self.add_cart).click()
        self.driver.find_element("xpath", self.shopping_cart).click()
        time.sleep(3)
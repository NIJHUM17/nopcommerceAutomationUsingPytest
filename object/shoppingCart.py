import time


class ShoppingCart:
    def __init__(self, driver, locator):
        self.driver = driver
        self.add_cart = locator["LOCATORS"]["add_cart"]
        self.shopping_cart_ = locator["LOCATORS"]["shopping_cart_"]

    def shopping_cart(self):
        time.sleep(1)
        self.driver.find_element("xpath", self.add_cart).click()
        self.driver.find_element("xpath", self.shopping_cart_).click()
        time.sleep(3)


import time


class CheckOut:

    def __init__(self, driver, locator):
        self.driver = driver
        # self.shop_cartBtn = locator["LOCATORS"]["shop_cart"]
        self.term_condition = locator["LOCATORS"]["term_condition"]
        self.checkout = locator["LOCATORS"]["checkout"]
        self.country = locator["LOCATORS"]["country"]
        self.city = locator["LOCATORS"]["city"]
        self.address_1 = locator["LOCATORS"]["address_1"]
        self.address_2 = locator["LOCATORS"]["address_2"]
        self.zipcode = locator["LOCATORS"]["zipcode"]
        self.phone = locator["LOCATORS"]["phone"]
        self.fax = locator["LOCATORS"]["fax"]
        self.continue_button = locator["LOCATORS"]["continue_button"]
        self.shipping_method = locator["LOCATORS"]["shipping_method"]
        self.payment_method = locator["LOCATORS"]["payment_method"]
        self.payment_info = locator["LOCATORS"]["payment_info"]
        self.confirm_order = locator["LOCATORS"]["confirm_order"]
        self.order_complete = locator["LOCATORS"]["order_complete"]

    def checkout_(self, checkout):
        # self.driver.find_element("xpath", self.shop_cartBtn).click()

        self.driver.find_element("xpath", self.term_condition).click()
        self.driver.find_element("xpath", self.checkout).click()
        self.driver.find_element("id", self.country).send_keys(checkout['country'])

        self.driver.find_element("id", self.city).send_keys(checkout['city'])

        self.driver.find_element("id", self.address_1).send_keys(checkout['Address1'])
        self.driver.find_element("id", self.address_2).send_keys(checkout['Address2'])

        self.driver.find_element("id", self.zipcode).send_keys(checkout['zipcode'])

        self.driver.find_element("id", self.phone).send_keys(checkout['phone'])
        self.driver.find_element("id", self.fax).send_keys(checkout['fax'])

        self.driver.find_element("xpath", self.continue_button).click()

        self.driver.find_element("xpath", self.shipping_method).click()
        self.driver.find_element("xpath", self.payment_method).click()
        self.driver.find_element("xpath", self.payment_info).click()
        self.driver.find_element("xpath", self.confirm_order).click()
        time.sleep(2)

        self.driver.find_element("xpath", self.order_complete).click()
        time.sleep(2)

import time
import locators
import test_data.reg_data
import test_data.checkout_data


class Checkout:

    def __init__(self, driver):
        self.driver = driver

    def checkout_button(self):
        time.sleep(4)
        self.driver.find_element("xpath", locators.term_condition).click()
        self.driver.find_element("xpath", locators.checkout).click()
        time.sleep(1)

    def billing_address(self):
        self.driver.find_element("id", locators.country).send_keys(test_data.checkout_data.country)
        self.driver.find_element("id", locators.city).send_keys(test_data.checkout_data.city)
        self.driver.find_element("id", locators.address_1).send_keys(test_data.checkout_data.address1)
        self.driver.find_element("id", locators.address_2).send_keys(test_data.checkout_data.address2)
        self.driver.find_element("id", locators.zipcode).send_keys(test_data.checkout_data.zip_code)
        self.driver.find_element("id", locators.phone).send_keys(test_data.checkout_data.phone_no)
        self.driver.find_element("id", locators.fax).send_keys(test_data.checkout_data.fax_no)
        time.sleep(1)

    def continue_button(self):
        self.driver.find_element("xpath", locators.continue_button).click()
        time.sleep(3)
        self.driver.find_element("xpath", locators.shipping_method).click()
        time.sleep(3)
        self.driver.find_element("xpath", locators.payment_method).click()
        time.sleep(3)
        self.driver.find_element("xpath", locators.payment_info).click()
        time.sleep(3)
        self.driver.find_element("xpath", locators.confirm_order).click()
        time.sleep(3)
        self.driver.find_element("xpath", locators.order_complete).click()

        time.sleep(4)
        self.driver.close()
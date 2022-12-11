import time
import locators
import testData.registrationData
import testData.checkoutData


class Checkout:

    def __init__(self, driver):
        self.driver = driver

    def checkout_button(self):
        time.sleep(4)
        self.driver.find_element("xpath", locators.term_condition).click()
        self.driver.find_element("xpath", locators.checkout).click()
        time.sleep(1)

    def billing_address(self):
        self.driver.find_element("id", locators.country).send_keys(testData.checkoutData.country)
        self.driver.find_element("id", locators.city).send_keys(testData.checkoutData.city)
        self.driver.find_element("id", locators.address_1).send_keys(testData.checkoutData.address1)
        self.driver.find_element("id", locators.address_2).send_keys(testData.checkoutData.address2)
        self.driver.find_element("id", locators.zipcode).send_keys(testData.checkoutData.zip_code)
        self.driver.find_element("id", locators.phone).send_keys(testData.checkoutData.phone_no)
        self.driver.find_element("id", locators.fax).send_keys(testData.checkoutData.fax_no)


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
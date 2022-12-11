import time

import locators
import testData.registrationData
import testData.loginData


class Login:

    def __init__(self, driver):
        self.driver = driver

    def log_in(self):
        time.sleep(2)
        self.driver.find_element("xpath", locators.log_in).click()
        time.sleep(1)

    def log_email(self):
        self.driver.find_element("id", locators.log_email).send_keys(testData.loginData.logemail)
        time.sleep(1)

    def log_password(self):
        self.driver.find_element("id", locators.log_password).send_keys(testData.loginData.logpass)
        time.sleep(3)

    def confirmLog(self):
        self.driver.find_element("xpath", locators.confirm_log).click()
        time.sleep(3)
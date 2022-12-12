import time

import locators
import test_data.reg_data
import test_data.login_data


class Login:

    def __init__(self, driver):
        self.driver = driver

    def log_in(self):
        time.sleep(2)
        self.driver.find_element("xpath", locators.log_in).click()
        time.sleep(1)

    def log_email(self):
        self.driver.find_element("id", locators.log_email).send_keys(test_data.login_data.logemail)
        time.sleep(1)

    def log_password(self):
        self.driver.find_element("id", locators.log_password).send_keys(test_data.login_data.logpass)
        time.sleep(3)

    def confirmLog(self):
        self.driver.find_element("xpath", locators.confirm_log).click()
        time.sleep(3)
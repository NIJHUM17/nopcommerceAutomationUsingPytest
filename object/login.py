import time


class Login:

    def __init__(self, driver, locator):

        self.driver = driver
        self.log = locator["LOCATORS"]["log_in"]
        self.log_email = locator["LOCATORS"]["log_email"]
        self.log_password = locator["LOCATORS"]["password"]
        self.confirm_log = locator["LOCATORS"]["confirm_log"]

    def log_in(self, log):
        self.driver.find_element("xpath", self.log).click()
        time.sleep(1)
        self.driver.find_element("id", self.log_email).send_keys(log['log_email'])
        self.driver.find_element("id", self.log_password).send_keys(log['password'])
        self.driver.find_element("xpath", self.confirm_log).click()

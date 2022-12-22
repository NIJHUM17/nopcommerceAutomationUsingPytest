
class Login:

    def __init__(self, driver, locator):

        self.driver = driver
        self.log = locator["LOCATORS"]["login"]
        self.log_email = locator["LOCATORS"]["email"]
        self.log_password = locator["LOCATORS"]["password"]
        self.confirm_log = locator["LOCATORS"]["confirm_log"]

    def log_in(self, email, log):
        self.driver.find_element("xpath", self.log).click()
        self.driver.find_element("id", self.log_email).send_keys(email)
        self.driver.find_element("id", self.log_password).send_keys(log['password'])
        self.driver.find_element("xpath", self.confirm_log).click()

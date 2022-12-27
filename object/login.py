
class Login:

    def __init__(self, driver, locator):
        self.driver = driver
        self.login = locator["LOCATORS"]["login"]
        self.email = locator["LOCATORS"]["email"]
        self.password = locator["LOCATORS"]["password"]
        self.confirm = locator["LOCATORS"]["confirm"]

    def log_in(self, log):
        self.driver.find_element("xpath", self.login).click()
        self.driver.find_element("id", self.email).send_keys(log['email'])
        self.driver.find_element("id", self.password).send_keys(log['password'])
        self.driver.find_element("xpath", self.confirm).click()

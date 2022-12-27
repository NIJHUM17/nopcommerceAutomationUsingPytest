class Register:

    def __init__(self, driver, locator):
        self.driver = driver
        self.reg = locator["LOCATORS"]["registration"]
        self.gender = locator["LOCATORS"]["gender"]
        self.first_name = locator["LOCATORS"]["first_name"]
        self.last_name = locator["LOCATORS"]["last_name"]
        self.date_of_birth = locator["LOCATORS"]["date_of_birth"]
        self.month_of_birth = locator["LOCATORS"]["month_of_birth"]
        self.year_of_birth = locator["LOCATORS"]["year_of_birth"]
        self.email = locator["LOCATORS"]["email"]
        self.company = locator["LOCATORS"]["company"]
        self.password = locator["LOCATORS"]["password"]
        self.confirm_password = locator["LOCATORS"]["confirm_password"]
        self.confirm_reg = locator["LOCATORS"]["confirm_reg"]
        self.continue_ = locator["LOCATORS"]["continue_"]

    def registration(self, reg):
        self.driver.find_element("xpath", self.reg).click()
        self.driver.find_element("xpath", self.gender).click()

        self.driver.find_element("id", self.first_name).send_keys(reg['firstName'])
        self.driver.find_element("id", self.last_name).send_keys(reg['lastName'])

        self.driver.find_element("name", self.date_of_birth).send_keys(reg['date'])
        self.driver.find_element("name", self.month_of_birth).send_keys(reg['month'])
        self.driver.find_element("name", self.year_of_birth).send_keys(reg['year'])
        self.driver.find_element("id", self.email).send_keys(reg['email'])
        self.driver.find_element("id", self.company).send_keys(reg['company'])
        self.driver.find_element("id", self.password).send_keys(reg['password'])
        self.driver.find_element("id", self.confirm_password).send_keys(reg['password'])
        self.driver.find_element("xpath", self.confirm_reg).click()
        self.driver.find_element("xpath", self.continue_).click()

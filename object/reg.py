

class Register:

    def __init__(self, driver, locator):
        self.x = None
        self.driver = driver
        self.reg = locator["LOCATORS"]["registration"]
        self.gender = locator["LOCATORS"]["gender"]
        self.firstname = locator["LOCATORS"]["first_name"]
        self.lastname = locator["LOCATORS"]["last_name"]
        self.birthday = locator["LOCATORS"]["date_of_birth"]
        self.birth_month = locator["LOCATORS"]["date_of_birthmonth"]
        self.birth_year = locator["LOCATORS"]["date_of_birthyear"]
        self.email = locator["LOCATORS"]["email"]
        self.company = locator["LOCATORS"]["company"]
        self.password = locator["LOCATORS"]["password"]
        self.confirm_pass = locator["LOCATORS"]["confirm_pass"]
        self.reg_confirm = locator["LOCATORS"]["reg_confirm"]
        self.logout = locator["LOCATORS"]["logout"]

    def registration(self, regwebsite):
        self.driver.find_element("xpath", self.regwebsite).click()
        self.driver.find_element("xpath", self.gender).click()


        self.driver.find_element("id", self.firstname).send_keys(regwebsite.registration_Data.firstname)

        self.driver.find_element("id", self.lastname).send_keys(regwebsite.registration_Data.lastname)

        self.driver.find_element("name", self.birthday).send_keys(regwebsite.registration_Data.date_of_birth)

        self.driver.find_element("name", self.birth_month).send_keys(regwebsite.registration_Data.date_of_birthmonth)

        self.driver.find_element("name", self.birth_year).send_keys(regwebsite.registration_Data.date_of_birthyear)
        self.driver.find_element("id", self.email).send_keys(regwebsite.registration_Data.email)
        self.driver.find_element("id", self.company).send_keys(regwebsite.registration_Data.company)
        self.driver.find_element("id", self.password).send_keys(regwebsite.registration_Data.password)
        self.driver.find_element("id", self.confirm_pass).send_keys(regwebsite.registration_Data.password)
        self.driver.find_element("xpath", self.reg_confirm).click()
        self.driver.find_element("xpath", self.logout).click()


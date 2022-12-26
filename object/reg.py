

class Register:

    def __init__(self, driver, locator):

        self.driver = driver
        self.registration = locator["LOCATORS"]["registration"]
        self.gender = locator["LOCATORS"]["gender"]
        self.first_name = locator["LOCATORS"]["first_name"]
        self.last_name = locator["LOCATORS"]["last_name"]
        self.birthday = locator["LOCATORS"]["date_of_birth"]
        self.birth_month = locator["LOCATORS"]["date_of_birthmonth"]
        self.birth_year = locator["LOCATORS"]["date_of_birthyear"]
        self.email = locator["LOCATORS"]["email"]
        self.company = locator["LOCATORS"]["company"]
        self.password = locator["LOCATORS"]["password"]
        self.confirm_pass = locator["LOCATORS"]["confirm_pass"]
        self.reg_confirm = locator["LOCATORS"]["reg_confirm"]
        self.logout = locator["LOCATORS"]["logout"]

    def registration(self, registration):
        self.driver.find_element("xpath", self.registration).click()
        self.driver.find_element("xpath", self.gender).click()
        self.driver.find_element("id", self.first_name).send_keys(registration.registration_Data.first_name)

        self.driver.find_element("id", self.last_name).send_keys(registration.registration_Data.last_name)

        self.driver.find_element("name", self.birthday).send_keys(registration.registration_Data.date_of_birth)

        self.driver.find_element("name", self.birth_month).send_keys(registration.registration_Data.date_of_birthmonth)

        self.driver.find_element("name", self.birth_year).send_keys(registration.registration_Data.date_of_birthyear)
        self.driver.find_element("id", self.email).send_keys(registration.registration_Data.email)
        self.driver.find_element("id", self.company).send_keys(registration.registration_Data.company)
        self.driver.find_element("id", self.password).send_keys(registration.registration_Data.password)
        self.driver.find_element("id", self.confirm_pass).send_keys(registration.registration_Data.password)
        self.driver.find_element("xpath", self.reg_confirm).click()
        self.driver.find_element("xpath", self.logout).click()


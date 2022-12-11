import time
import locators
import testData.registrationData


class Registration:

    def __init__(self, driver):
        self.driver = driver

    def registration(self):
        time.sleep(2)
        self.driver.find_element("xpath", locators.registration).click()

    def gender(self):
        self.driver.find_element("xpath", locators.gender).click()

    def name(self):
        self.driver.find_element("id", locators.first_name).send_keys(testData.registrationData.firstname)
        self.driver.find_element("id", locators.last_name).send_keys(testData.registrationData.lastname)

    def dob(self):
        self.driver.find_element("name", locators.date_of_birth).send_keys(testData.registrationData.day)
        self.driver.find_element("name", locators.date_of_birthmonth).send_keys(testData.registrationData.month)
        self.driver.find_element("name", locators.date_of_birthyear).send_keys(testData.registrationData.year)
        time.sleep(2)

    def email(self):
        self.driver.find_element("id", locators.email).send_keys(testData.registrationData.myemail)
        time.sleep(2)

    def company(self):
        self.driver.find_element("id", locators.company).send_keys(testData.registrationData.mycompany)
        time.sleep(1)


    def password(self):
        self.driver.find_element("id", locators.password).send_keys(testData.registrationData.mypass)
        time.sleep(1)

    def Confirmpass(self):
        self.driver.find_element("id", locators.confirm_pass).send_keys(testData.registrationData.mypass)
        time.sleep(1)

    def RegConfirm(self):
        self.driver.find_element("xpath", locators.reg_confirm).click()
        time.sleep(2)

    def Logout(self):
        time.sleep(5)
        self.driver.find_element("xpath", locators.logout).click()
        time.sleep(1)
import time
import locators
import test_data.reg_data


class Registration:

    def __init__(self, driver):
        self.driver = driver

    def registration(self):
        time.sleep(2)
        self.driver.find_element("xpath", locators.registration).click()

    def gender(self):
        self.driver.find_element("xpath", locators.gender).click()

    def name(self):
        self.driver.find_element("id", locators.first_name).send_keys(test_data.reg_data.firstname)
        self.driver.find_element("id", locators.last_name).send_keys(test_data.reg_data.lastname)

    def dob(self):
        self.driver.find_element("name", locators.date_of_birth).send_keys(test_data.reg_data.day)
        self.driver.find_element("name", locators.date_of_birthmonth).send_keys(test_data.reg_data.month)
        self.driver.find_element("name", locators.date_of_birthyear).send_keys(test_data.reg_data.year)
        time.sleep(2)

    def email(self):
        self.driver.find_element("id", locators.email).send_keys(test_data.reg_data.myemail)
        time.sleep(2)

    def company(self):
        self.driver.find_element("id", locators.company).send_keys(test_data.reg_data.mycompany)
        time.sleep(1)


    def password(self):
        self.driver.find_element("id", locators.password).send_keys(test_data.reg_data.mypass)
        time.sleep(1)

    def Confirmpass(self):
        self.driver.find_element("id", locators.confirm_pass).send_keys(test_data.reg_data.mypass)
        time.sleep(1)

    def RegConfirm(self):
        self.driver.find_element("xpath", locators.reg_confirm).click()
        time.sleep(2)

    def Logout(self):
        time.sleep(5)
        self.driver.find_element("xpath", locators.logout).click()
        time.sleep(1)
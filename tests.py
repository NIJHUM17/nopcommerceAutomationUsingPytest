import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from objects.open_browser import OpenBrowser
from objects.registration import Registration
from objects.login import Login
from objects.search import Search
from objects.shopping_cart import Shopping_cart
from objects.checkout import Checkout


class TestFullCycle(unittest.TestCase):
    s = Service("D:/Python/PyTest Excercise/nopcommerceAutomationUsingPytest/chrome_driver/chromedriver.exe")
    driver = webdriver.Chrome(service=s)

    def test_1(self):
        open_browser = OpenBrowser(self.driver)
        open_browser.open_webBrowser()

    def test_2(self):
        reg = Registration(self.driver)
        reg.registration()
        reg.gender()
        reg.name()
        reg.dob()
        reg.email()
        reg.company()
        reg.password()
        reg.Confirmpass()
        reg.RegConfirm()
        reg.Logout()

    def test_3(self):
        log = Login(self.driver)
        log.log_in()
        log.log_email()
        log.log_password()
        log.confirmLog()

    def test_4(self):
        search = Search(self.driver)
        search.searching()
        search.searchproduct()
        search.searchinside()

    def test_5(self):
        cart = Shopping_cart(self.driver)
        cart.add_cart()
        cart.Shop_cart()

    def test_6(self):
        checkout = Checkout(self.driver)
        checkout.checkout_button()
        checkout.billing_address()
        checkout.continue_button()

    if __name__ == '__main__':
        unittest.main()


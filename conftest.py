import configparser

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def config():
    _file = "D:\\Python\\PyTestExcercise\\nopcommerceAutomationUsingPytest\\data_house.ini"
    parser = configparser.ConfigParser()
    parser.read(_file)
    return parser


@pytest.fixture(scope='function')
def locator():
    _file = "D:\\Python\\PyTestExcercise\\nopcommerceAutomationUsingPytest\\data_house.ini"
    parser = configparser.ConfigParser()
    parser.read(_file)
    return parser


@pytest.fixture(scope='function')
def driver():
    _chromedriver = "D:\\Python\\PyTestExcercise\\nopcommerceAutomationUsingPytest\\driver\\chromedriver.exe"
    s = Service(_chromedriver)
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    driver.quit()

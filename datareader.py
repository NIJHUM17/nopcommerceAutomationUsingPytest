import configparser
import os


class Data:

    def data(self):
        _file = "D:\\Python\\PyTestExcercise\\nopcommerceAutomationUsingPytest\\data_house.ini"
        parser = configparser.ConfigParser()
        parser.read(_file)
        return parser

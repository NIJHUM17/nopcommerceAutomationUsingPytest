import time
import url

class OpenBrowser:

    def __init__(self, driver, config):
        self.driver = driver
        self.webLink = config["https://demo.nopcommerce.com/"]

    def open_webBrowser(self):
        url = self.webLink
        self.driver.get(url)
        self.driver.implicitly_wait(20)
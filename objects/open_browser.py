import time

class OpenBrowser:

    def __init__(self, driver, config):
        self.driver = driver
        self.webLink = config["url"]

    def open_webBrowser(self):
        url = self.webLink
        self.driver.get(url)
        self.driver.implicitly_wait(20)
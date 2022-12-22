

class OpenBrowser:

    def __init__(self, driver, config):
        self.driver = driver
        self.webLink = config["common info"]["url"]

    def open_webBrowser(self):
        url = self.webLink
        self.driver.get(url)
        self.driver.implicitly_wait(20)

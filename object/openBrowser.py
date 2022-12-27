class OpenBrowser:

    def __init__(self, driver, config):
        self.driver = driver
        self.webLink = config["web link"]["base_url"]

    def open_webBrowser(self):
        base_url = self.webLink
        self.driver.get(base_url)
        self.driver.implicitly_wait(20)

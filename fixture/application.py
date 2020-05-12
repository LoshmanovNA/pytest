from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, browser, url):
        if browser == "local":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = self.driver_setup(browser=browser, version="72.0")
        elif browser == "chrome":
            self.wd = self.driver_setup(browser=browser, version="80.0")
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.url = url

    @staticmethod
    def driver_setup(browser, version):
        capabilities = {
            "browserName": browser,
            "version": version,
            "enableVNC": True,
            "enableVideo": False
        }
        driver = webdriver.Remote(command_executor="127.0.0.1:4444/wd/hub", desired_capabilities=capabilities)
        driver.maximize_window()
        return driver

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.url)

    def destroy(self):
        self.wd.quit()

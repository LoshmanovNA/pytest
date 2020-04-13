from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
import sys


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        os = sys.platform
        if os == "win32":
            wd.get("http://localhost/addressbook/")
        else:
            wd.get("http://localhost:8080/addressbook/")

    def destroy(self):
        self.wd.quit()

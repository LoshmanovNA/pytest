from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SessionHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in(self):
        return True if self.wd.find_elements_by_link_text("Logout") else False

    def is_logged_in_as(self, username):
        return self._get_logged_user() == username

    def login(self, username, password):
        self.app.open_home_page()
        self.wd.implicitly_wait(10)
        self.wd.find_element_by_name("user").clear()
        self.wd.find_element_by_name("user").send_keys(username)
        self.wd.find_element_by_name("pass").click()
        self.wd.find_element_by_name("pass").clear()
        self.wd.find_element_by_name("pass").send_keys(password)
        self.wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()

    def _get_logged_user(self):
        return self.wd.find_element_by_css_selector("#container form b").text[1:-1]



from selenium.webdriver.support.ui import Select
import os.path


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def create(self, contact):
        self._open_add_contact_page()
        self._fill_form(contact)
        self._load_image()
        self._submit_form()
        self._go_to_homepage()

    def delete_first_contact(self):
        self.wd.find_element_by_name("selected[]").click()
        self.wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.wd.switch_to_alert().accept()

    def edit_first_contact(self, contact):
        self.wd.find_element_by_name("selected[]").click()
        self.wd.find_element_by_xpath("//img[@alt='Edit']]").click()
        self._fill_form(contact)
        self._update_form()
        self._go_to_homepage()

    def _fill_form(self, contact):
        # Person data
        self.wd.find_element_by_name("firstname").clear()
        self.wd.find_element_by_name("firstname").send_keys(contact.first_name)
        self.wd.find_element_by_name("middlename").clear()
        self.wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        self.wd.find_element_by_name("lastname").clear()
        self.wd.find_element_by_name("lastname").send_keys(contact.last_name)
        self.wd.find_element_by_name("nickname").clear()
        self.wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # Company data
        self.wd.find_element_by_name("title").clear()
        self.wd.find_element_by_name("title").send_keys(contact.title)
        self.wd.find_element_by_name("company").clear()
        self.wd.find_element_by_name("company").send_keys(contact.company)
        self.wd.find_element_by_name("address").clear()
        self.wd.find_element_by_name("address").send_keys(contact.address)
        # Phone numbers
        self.wd.find_element_by_name("home").clear()
        self.wd.find_element_by_name("home").send_keys(contact.home_phone)
        self.wd.find_element_by_name("mobile").clear()
        self.wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        self.wd.find_element_by_name("work").clear()
        self.wd.find_element_by_name("work").send_keys(contact.work_phone)
        self.wd.find_element_by_name("fax").clear()
        self.wd.find_element_by_name("fax").send_keys(contact.fax)
        self.wd.find_element_by_name("email").clear()
        self.wd.find_element_by_name("email").send_keys(contact.email_1)
        self.wd.find_element_by_name("email2").clear()
        self.wd.find_element_by_name("email2").send_keys(contact.email_2)
        self.wd.find_element_by_name("email3").clear()
        self.wd.find_element_by_name("email3").send_keys(contact.email_3)
        self.wd.find_element_by_name("homepage").clear()
        self.wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # Select date of birth
        Select(self.wd.find_element_by_name("bday")).select_by_visible_text(contact.day_of_birth)
        Select(self.wd.find_element_by_name("bmonth")).select_by_visible_text(contact.month_of_birth)
        self.wd.find_element_by_name("byear").clear()
        self.wd.find_element_by_name("byear").send_keys(contact.year_of_birth)
        # Select anniversary
        Select(self.wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        Select(self.wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        self.wd.find_element_by_name("ayear").clear()
        self.wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        # Second address and phone
        self.wd.find_element_by_name("address2").clear()
        self.wd.find_element_by_name("address2").send_keys(contact.address_2)
        self.wd.find_element_by_name("phone2").clear()
        self.wd.find_element_by_name("phone2").send_keys(contact.phone_2)
        self.wd.find_element_by_name("notes").clear()
        # Notes
        self.wd.find_element_by_name("notes").send_keys(contact.notes)

    def _open_add_contact_page(self):
        self.wd.find_element_by_link_text("add new").click()

    def _submit_form(self):
        self.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def _update_form(self):
        self.wd.find_element_by_name("update").click()

    def _go_to_homepage(self):
        self.wd.find_element_by_link_text("home page").click()

    def _load_image(self):
        img_path = r"\media\pic.jpg" if os.getcwd().startswith(r"\/") else r"/media/pic.jpg"
        path = os.getcwd() + img_path
        self.wd.find_element_by_name("photo").send_keys(path)

    def _select_group(self):
        pass


# if __name__ == '__main__':
#     print(os.getcwd() + '\media\pic.jpg')

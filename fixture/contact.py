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
        self.app.open_home_page()
        self._select_first_contact()
        self._click_delete_button()
        self._accept_action_in_alert()

    def edit_first_contact(self, contact):
        self.app.open_home_page()
        self._select_first_contact()
        self._click_edit_button()
        self._fill_form(contact)
        self._update_form()
        self._go_to_homepage()

    def _accept_action_in_alert(self):
        self.wd.switch_to_alert().accept()

    def _click_delete_button(self):
        self.wd.find_element_by_xpath("//input[@value='Delete']").click()

    def _click_edit_button(self):
        self.wd.find_element_by_css_selector("#maintable a[href*='edit']").click()

    def _is_select_value_present(self, field_name, value):
        if value:
            Select(self.wd.find_element_by_name(field_name)).select_by_visible_text(value)

    def _is_text_value_present(self, field_name, value):
        if value:
            self.wd.find_element_by_name(field_name).clear()
            self.wd.find_element_by_name(field_name).send_keys(value)

    def _fill_form(self, contact):
        # Person data
        self._is_text_value_present("firstname", contact.first_name)
        self._is_text_value_present("middlename", contact.middle_name)
        self._is_text_value_present("lastname", contact.last_name)
        self._is_text_value_present("nickname", contact.nickname)
        # Company data
        self._is_text_value_present("title", contact.title)
        self._is_text_value_present("company", contact.company)
        self._is_text_value_present("address", contact.address)
        # Phone numbers
        self._is_text_value_present("home", contact.home_phone)
        self._is_text_value_present("mobile", contact.mobile_phone)
        self._is_text_value_present("work", contact.work_phone)
        self._is_text_value_present("fax", contact.fax)
        self._is_text_value_present("email", contact.email_1)
        self._is_text_value_present("email2", contact.email_2)
        self._is_text_value_present("email3", contact.email_3)
        self._is_text_value_present("homepage", contact.homepage)
        # Select date of birth
        self._is_select_value_present("bday", contact.day_of_birth)
        self._is_select_value_present("bmonth", contact.month_of_birth)
        self._is_text_value_present("byear", contact.year_of_birth)
        # Select anniversary
        self._is_select_value_present("aday", contact.anniversary_day)
        self._is_select_value_present("amonth", contact.anniversary_month)
        self._is_text_value_present("ayear", contact.anniversary_year)
        # Second address and phone
        self._is_text_value_present("address2", contact.address_2)
        self._is_text_value_present("phone2", contact.phone_2)
        # Notes
        self._is_text_value_present("notes", contact.notes)

    def _go_to_homepage(self):
        self.wd.find_element_by_link_text("home page").click()

    def _load_image(self):
        img_path = r"\media\pic.jpg" if os.getcwd().startswith(r"\/") else r"/media/pic.jpg"
        path = os.getcwd() + img_path
        self.wd.find_element_by_name("photo").send_keys(path)

    def _open_add_contact_page(self):
        self.wd.find_element_by_link_text("add new").click()

    def _submit_form(self):
        self.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def _select_first_contact(self):
        self.wd.find_element_by_name("selected[]").click()

    def _select_group(self):
        pass

    def _update_form(self):
        self.wd.find_element_by_name("update").click()


# if __name__ == '__main__':
#     print(os.getcwd() + '\media\pic.jpg')

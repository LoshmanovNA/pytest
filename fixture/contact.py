from selenium.webdriver.support.ui import Select
from model.contact import Contact
import sys
import os
import re


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
        self.contacts_cache = None

    def count(self):
        return len(self.wd.find_elements_by_name("selected[]"))

    def delete_first_contact(self, index):
        self.delete_contact_by_index(index)

    def delete_contact_by_index(self, index):
        self._go_to_homepage()
        self._select_contact_by_index(index)
        self._click_delete_button()
        self._accept_action_in_alert()
        self.contacts_cache = None

    def delete_contact_by_id(self, id):
        self._go_to_homepage()
        self._select_contact_by_id(id)
        self._click_delete_button()
        self._accept_action_in_alert()
        self.contacts_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        self._go_to_homepage()
        self._select_contact_by_index(index)
        self._click_edit_button()
        self._fill_form(contact)
        # time.sleep(3)
        self._update_form()
        # time.sleep(3)
        self._go_to_homepage()
        self.contacts_cache = None

    def edit_contact_by_id(self, id, contact):
        self._go_to_homepage()
        self._select_contact_by_id(id)
        self._click_edit_button()
        self._fill_form(contact)
        # time.sleep(3)
        self._update_form()
        # time.sleep(3)
        self._go_to_homepage()
        self.contacts_cache = None

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            self._go_to_homepage()
            self.contacts_cache = []
            for row in self.wd.find_elements_by_name("entry"):
                cellc = row.find_elements_by_tag_name("td")
                id = cellc[0].find_element_by_tag_name("input").get_attribute("value")
                last_name = cellc[1].text
                first_name = cellc[2].text
                address = cellc[3].text
                all_emails = cellc[4].text
                all_phones = cellc[5].text
                self.contacts_cache.append(Contact(id=id,
                                                   first_name=first_name,
                                                   last_name=last_name,
                                                   address=address,
                                                   all_emails_from_home_page=all_emails,
                                                   all_phones_from_home_page=all_phones))
        return list(self.contacts_cache)

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        first_name = self.wd.find_element_by_name("firstname").get_attribute("value")
        last_name = self.wd.find_element_by_name("lastname").get_attribute("value")
        id = self.wd.find_element_by_name("id").get_attribute("value")
        address = self.wd.find_element_by_name("address").get_attribute("value")
        email_1 = self.wd.find_element_by_name("email").get_attribute("value")
        email_2 = self.wd.find_element_by_name("email2").get_attribute("value")
        email_3 = self.wd.find_element_by_name("email3").get_attribute("value")
        home_phone = self.wd.find_element_by_name("home").get_attribute("value")
        work_phone = self.wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = self.wd.find_element_by_name("mobile").get_attribute("value")
        phone_2 = self.wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, id=id,
                       address=address, email_1=email_1, email_2=email_2, email_3=email_3,
                       home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, phone_2=phone_2)

    def get_contact_from_view_page(self, index):
        self.open_contact_view_by_index(index)
        text = self.wd.find_element_by_id("content").text
        print(text)
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        phone_2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, phone_2=phone_2)

    def open_contact_to_edit_by_index(self, index):
        self._go_to_homepage()
        row = self.wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        self._go_to_homepage()
        row = self.wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def _accept_action_in_alert(self):
        self.wd.switch_to.alert.accept()

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
        if not (self.wd.current_url.endswith("/index.php") and
                self.wd.find_elements_by_css_selector("#maintable a[href*='edit']")):
            self.wd.find_element_by_partial_link_text("home").click()

    def _load_image(self):
        os_type = sys.platform
        try:
            img_path = r"\test\media\pic.jpg" if os_type == "win32" else r"/test/media/pic.jpg"
            path = os.getcwd() + img_path
            self.wd.find_element_by_name("photo").send_keys(path)
            return
        except:
            img_path = r"\media\pic.jpg" if os_type == "win32" else r"/media/pic.jpg"
            path = os.getcwd() + img_path
            self.wd.find_element_by_name("photo").send_keys(path)

    def _open_add_contact_page(self):
        self.wd.find_element_by_link_text("add new").click()

    def _submit_form(self):
        self.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def _select_contact_by_index(self, index):
        self.wd.find_elements_by_name("selected[]")[index].click()

    def _select_contact_by_id(self, id):
        self.wd.find_element_by_css_selector(f"input[value='{id}']").click()

    def _select_group(self):
        pass

    def _update_form(self):
        self.wd.find_element_by_css_selector("input[value='Update']").click()

# if __name__ == '__main__':
#     print(os.getcwd() + '\media\pic.jpg')

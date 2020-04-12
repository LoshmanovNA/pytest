

class GroupHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def create(self, group_data):
        self._open_groups_page()
        self._init_group_creation()
        self._fill_group_form(group_data)
        self._submit_new_group()
        self._return_to_groups_page()

    def delete_first_group(self):
        self._open_groups_page()
        self._select_first_group()
        self._click_delete_button()
        self._return_to_groups_page()

    def edit_first_group(self, group_data):
        self._open_groups_page()
        self._select_first_group()
        self._click_edit_button()
        self._fill_group_form(group_data)
        self._update_group()
        self._return_to_groups_page()

    def _click_delete_button(self):
        self.wd.find_element_by_name("delete").click()

    def _click_edit_button(self):
        self.wd.find_element_by_name("edit").click()

    def _init_group_creation(self):
        self.wd.find_element_by_name("new").click()

    def _is_value_present(self, field_name, value):
        if value:
            self.wd.find_element_by_name(field_name).clear()
            self.wd.find_element_by_name(field_name).send_keys(value)

    def _fill_group_form(self, group_data):
        self._is_value_present("group_name", group_data.name)
        self._is_value_present("group_header", group_data.header)
        self._is_value_present("group_footer", group_data.footer)

    def _open_groups_page(self):
        self.wd.find_element_by_link_text("groups").click()

    def _return_to_groups_page(self):
        self.wd.find_element_by_link_text("group page").click()

    def _select_first_group(self):
        self.wd.find_element_by_name("selected[]").click()

    def _submit_new_group(self):
        self.wd.find_element_by_name("submit").click()

    def _update_group(self):
        self.wd.find_element_by_name("update").click()



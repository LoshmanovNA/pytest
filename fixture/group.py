from model.group import Group


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
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        self._open_groups_page()
        self._select_group_by_index(index)
        self._click_delete_button()
        self._return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        self._open_groups_page()
        self._select_group_by_id(id)
        self._click_delete_button()
        self._return_to_groups_page()
        self.group_cache = None

    def edit_first_group(self, group_data):
        self.edit_group_by_index(0, group_data)

    def edit_group_by_index(self, index, group_data):
        self._open_groups_page()
        self._select_group_by_index(index)
        self._click_edit_button()
        self._fill_group_form(group_data)
        self._update_group()
        self._return_to_groups_page()
        self.group_cache = None

    def count(self):
        self._open_groups_page()
        return len(self.wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_groups_list(self):
        if self.group_cache is None:
            self._open_groups_page()
            self.group_cache = []
            for element in self.wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, element_id=id))
        return list(self.group_cache)

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
        if not (self.wd.current_url.endswith("/group.php") and self.wd.find_elements_by_name("new")):
            self.wd.find_element_by_link_text("groups").click()

    def _return_to_groups_page(self):
        self.wd.find_element_by_link_text("group page").click()

    def _select_group_by_index(self, index):
        self.wd.find_elements_by_name("selected[]")[index].click()

    def _select_group_by_id(self, id):
        self.wd.find_element_by_css_selector(f"input[value='{id}']").click()

    def _submit_new_group(self):
        self.wd.find_element_by_name("submit").click()

    def _update_group(self):
        self.wd.find_element_by_name("update").click()



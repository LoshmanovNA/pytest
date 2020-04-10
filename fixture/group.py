

class GroupHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def create(self, group):
        self._open_groups_page()
        self._init_group_creation()
        self._fill_group_form(group)
        self._submit_new_group()
        self._return_to_groups_page()

    def delete_first_group(self):
        self._open_groups_page()
        self.wd.find_element_by_name("selected[]").click()
        self.wd.find_element_by_name("delete").click()
        self._return_to_groups_page()

    def edit_first_group(self, group):
        self._open_groups_page()
        self.wd.find_element_by_name("selected[]").click()
        self.wd.find_element_by_name("edit").click()
        self._fill_group_form(group)
        self._update_group()
        self._return_to_groups_page()

    def _open_groups_page(self):
        self.wd.find_element_by_link_text("groups").click()

    def _init_group_creation(self):
        self.wd.find_element_by_name("new").click()

    def _fill_group_form(self, group):
        self.wd.find_element_by_name("group_name").clear()
        self.wd.find_element_by_name("group_name").send_keys(group.name)
        self.wd.find_element_by_name("group_header").clear()
        self.wd.find_element_by_name("group_header").send_keys(group.header)
        self.wd.find_element_by_name("group_footer").clear()
        self.wd.find_element_by_name("group_footer").send_keys(group.footer)

    def _submit_new_group(self):
        self.wd.find_element_by_name("submit").click()

    def _update_group(self):
        self.wd.find_element_by_name("update").click()

    def _return_to_groups_page(self):
        self.wd.find_element_by_link_text("group page").click()



class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def change_field_value(self, field_name, input_text):
        wd = self.app.wd
        if input_text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(input_text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def create(self, group):
        wd = self.app.wd
        ## Open group page
        self.open_groups_page()
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group create form
        self.fill_group_form(group)
        #Submin group creation
        wd.find_element_by_name("submit").click()
        ## Return to mainpage after group creation
        self.return_to_groups_page()

    def check_group_on_group_page(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete(self):
        wd = self.app.wd
        ## Open group page
        self.open_groups_page()
        ## Find group on group_page
        self.check_group_on_group_page()
        ## Delete group
        wd.find_element_by_name("delete").click()
        ## Return to mainpage after group creation
        self.return_to_groups_page()

    def edit(self, new_group_data):
        wd = self.app.wd
        ## Open group page
        self.open_groups_page()
        ## Find group on group_page
        self.check_group_on_group_page()
        ## Edit group
        wd.find_element_by_name("edit").click()
        # Fill group create form
        self.fill_group_form(new_group_data)
        #Submin group update
        wd.find_element_by_name("update").click()
        ## Return to mainpage after group creation
        self.return_to_groups_page()


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

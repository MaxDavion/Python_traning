

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

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

    def edit(self, group):
        wd = self.app.wd
        ## Open group page
        self.open_groups_page()
        ## Find group on group_page
        self.check_group_on_group_page()
        ## Edit group
        wd.find_element_by_name("edit").click()
        # Fill group create form
        self.fill_group_form(group)
        #Submin group update
        wd.find_element_by_name("update").click()
        ## Return to mainpage after group creation
        self.return_to_groups_page()


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


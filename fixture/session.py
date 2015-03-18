

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user, password):
        wd = self.app.wd
        ## Open login page
        self.app.open_home_page()
        ## Autorization
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, user):
        wd = self.app.wd
        return wd.find_element_by_xpath("//*[@id='top']/form/b").text == "(" + user + ")"

    def ensure_login(self, user, password):
        wd = self.app.wd
        if self.is_logged_in():
            if is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user, password)






    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

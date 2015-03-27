# -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webdriver import WebDriver
from session import SessionHelper
from group import GroupHelper
from contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
#        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://skyrim/addressbook/")

    def go_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False




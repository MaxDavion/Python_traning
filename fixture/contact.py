# -*- coding: utf-8 -*-

from selenium.webdriver.support.select import Select
import selenium.webdriver.support.wait
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, insert_text):
        wd = self.app.wd
        if insert_text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(insert_text)

    def change_select_value(self, field_name, insert_value):
        wd = self.app.wd
        if insert_value is not None:
            select = Select(wd.find_element_by_name(field_name))
            select.select_by_value(insert_value)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_select_value('bday', contact.bday)
        self.change_select_value('bmonth', contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_select_value('aday', contact.aday)
        self.change_select_value('amonth', contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address_secondary)
        self.change_field_value("phone2", contact.phone_secondary)
        self.change_field_value("notes", contact.notes)


    def create(self, contact):
        wd = self.app.wd
        ## Init contact creation
        wd.find_element_by_link_text("add new").click()
        ## Fill contact form
        self.fill_contact_form(contact)
        ##Submin contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        ## Return to main page  after contact creation
        self.return_to_main_page()

    def delete_from_main_page(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def click_edit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def delete_from_contact_form(self):
        wd = self.app.wd
        ## Click on Edit contact button
        self.click_edit_contact()
        ## Click delete button
        wd.find_element_by_xpath("//*[@id='content']/form[2]/input[2]").click()


    def edit(self, new_contact_data):
        wd = self.app.wd
        ## Click on Edit contact button
        self.click_edit_contact()
        ## Fill contact form
        self.fill_contact_form(new_contact_data)
        ##Submin contact edit
        wd.find_element_by_xpath("//*[@id='content']/form[1]/input[22]").click()
        ## Return to main page  after contact creation
        self.return_to_main_page()

    def return_to_main_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    # Метод,для получения списка контактов с главной страницы
    def get_contact_list(self):
        wd = self.app.wd
        self.app.go_to_home_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("tr[name=entry]"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            lastname = element.find_element_by_css_selector("td:nth-child(2)").text
            firstname = element.find_element_by_css_selector("td:nth-child(3)").text
            contacts.append(Contact(id=id, lastname=lastname, firstname=firstname))
        return contacts



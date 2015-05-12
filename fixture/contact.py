# -*- coding: utf-8 -*-

from selenium.webdriver.support.select import Select
import selenium.webdriver.support.wait
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

# -------------------------------------------------------------

# Методы относящиеся к заполнению формы добавления\редактирования контакта.

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
        self.change_field_value("email", contact.email)
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

# -------------------------------------------------------------

# Методы относящиеся к выполнению действий с контактом

# Создание контакта
    def create(self, contact):
        wd = self.app.wd
        ## Init contact creation
        self.open_add_contact_page(wd)
        ## Fill contact form
        self.fill_contact_form(contact)
        ##Submin contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        ## Return to main page  after contact creation
        self.return_to_main_page()
        self.conact_cache = None  # очишаем кеш со списком групп на странице групп

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.go_to_home_page()
        wd.find_elements_by_xpath("//*[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.go_to_home_page()
        wd.find_element_by_css_selector("[href='edit.php?id=%s']" % id).click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.go_to_home_page()
        wd.find_elements_by_xpath("//*[@id='maintable']/tbody/tr/td[7]/a/img")[index].click()

    def delete_first_from_main_page(self):
        self.delete_by_index_from_main_page(0)

    def delete_by_index_from_main_page(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None  # очишаем кеш со списком групп на странице групп

    def delete_by_id_from_main_page(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None  # очишаем кеш со списком групп на странице групп

    def delete_by_index_from_contact_form(self, index):
        wd = self.app.wd
        ## Click on Edit contact button
        self.open_contact_to_edit_by_index(index)
        ## Click delete button
        wd.find_element_by_xpath("//*[@id='content']/form[2]/input[2]").click()
        self.conact_cache = None  # очишаем кеш со списком групп на странице групп

    def delete_by_id_from_contact_form(self, id):
        wd = self.app.wd
        ## Click on Edit contact button
        self.open_contact_to_edit_by_id(id)
        ## Click delete button
        wd.find_element_by_xpath("//*[@id='content']/form[2]/input[2]").click()
        self.conact_cache = None  # очишаем кеш со списком групп на странице групп

    def edit_first_contact(self, new_contact_data):
        self.edit_by_index(new_contact_data, 0)

    def edit_by_index(self, new_contact_data, index):
        wd = self.app.wd
        ## Click on Edit contact button
        self.open_contact_to_edit_by_index(index)
        ## Fill contact form
        self.fill_contact_form(new_contact_data)
        ##Submin contact edit
        wd.find_element_by_xpath("//*[@id='content']/form[1]/input[22]").click()
        ## Return to main page  after contact creation
        self.return_to_main_page()
        self.conact_cache = None  # очишаем кеш со списком групп на странице групп

    def edit_by_id(self, new_contact_data, id):
        wd = self.app.wd
        ## Click on Edit contact button
        self.open_contact_to_edit_by_id(id)
        ## Fill contact form
        self.fill_contact_form(new_contact_data)
        ##Submin contact edit
        wd.find_element_by_xpath("//*[@id='content']/form[1]/input[22]").click()
        ## Return to main page  after contact creation
        self.return_to_main_page()
        self.conact_cache = None  # очишаем кеш со списком групп на странице групп

# -------------------------------------------------------------

# Методы навигации

    def return_to_main_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_add_contact_page(self, wd):
        if not wd.current_url.endswith("/edit.php"):
            wd.find_element_by_link_text("add new").click()

# -------------------------------------------------------------

# Прочие вспомогательные методы сбора информации:

    # Метод возвращает кол-во контактов с главной страницы
    def count(self):
        wd = self.app.wd
        self.app.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    conact_cache = None  # Переменная для хранения кеша списка объектов contact на главной странице

    # Метод,для получения списка, состоящего из объектов Contact, с главной страницы
    def get_contact_list(self):
        if self.conact_cache is None:
            wd = self.app.wd
            self.app.go_to_home_page()  # Переходим на главную страницу
            self.conact_cache = []  # Создаем пустой список, для включения в него найденных на странице контактов
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):  # Для каждого контакта с главной страницы берем  доступные атрибуты и помещаем в список
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = element.find_element_by_css_selector("td:nth-child(2)").text
                firstname = element.find_element_by_css_selector("td:nth-child(3)").text
                address = element.find_element_by_css_selector("td:nth-child(4)").text
                all_emails = element.find_element_by_css_selector("td:nth-child(5)").text
                all_phones = element.find_element_by_css_selector("td:nth-child(6)").text
                self.conact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname,
                                                 address=address, all_emails_from_home_page=all_emails,
                                                 all_phones_from_home_page=all_phones))
        return list(self.conact_cache)  # Возвращаем копию полученного списка контактов

    # Метод,для получения атрибутов контакта со страницы редактирования контакта.
    def get_contact_details_from_edit_page(self):
        wd = self.app.wd
        id = wd.find_element_by_name("id").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone_secondary = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, lastname=lastname, firstname=firstname, address=address,
                       email=email, email2=email2, email3=email3,
                       home=home, mobile=mobile, work=work, phone_secondary=phone_secondary)

    # Метод,для получения атрибутов контакта со страницы просмотра контакта.
    def get_contact_details_from_view_page(self):
        wd = self.app.wd
        all_contact_details = wd.find_element_by_id("content").text
        home = re.search('H: (.*)',all_contact_details).group(1)
        mobile = re.search('M: (.*)',all_contact_details).group(1)
        work = re.search('W: (.*)',all_contact_details).group(1)
        phone_secondary = re.search('P: (.*)', all_contact_details).group(1)
        return Contact(home=home, mobile=mobile, work=work, phone_secondary=phone_secondary)

    # Метод,для получения списков месяцев со страницы создания\редактирования контакта
    def get_month_from_create_page(self):
        wd = self.app.wd
        self.open_add_contact_page()
        month = wd.find_element_by_xpath("//*[@id='content']/form/select[2]").text
        return month.split("\n")


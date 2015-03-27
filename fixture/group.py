# -*- coding: utf-8 -*-
from model.group import Group

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
        self.group_cache = None  # очишаем кеш со списком групп на странице групп

    # Метод отмечает группу на странице группы, в качестве параметра передается index группы в переменной, group_cache
    def check_group_on_group_page(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_group(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        ## Open group page
        self.open_groups_page()
        ## Find group on group_page
        self.check_group_on_group_page(index)
        ## Delete group
        wd.find_element_by_name("delete").click()
        ## Return to mainpage after group creation
        self.return_to_groups_page()
        self.group_cache = None  # очишаем кеш со списком групп на странице групп

    def edit_first_group(self, new_group_data):
        self.delete_by_index(new_group_data, 0)

    def edit_by_index(self, new_group_data, index):
        wd = self.app.wd
        ## Open group page
        self.open_groups_page()
        ## Find group on group_page
        self.check_group_on_group_page(index)
        ## Edit group
        wd.find_element_by_name("edit").click()
        # Fill group create form
        self.fill_group_form(new_group_data)
        #Submin group update
        wd.find_element_by_name("update").click()
        ## Return to mainpage after group creation
        self.return_to_groups_page()
        self.group_cache = None  # очишаем кеш со списком групп на странице групп

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    # Метод возвращает кол-во групп со страницы групп
    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None  # Переменная для хранения списка групп на странице групп

    # Метод, для получения списка групп (id, name) со страницы групп
    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()  # Переходим на страницу групп
            self.group_cache = []  # Создаем пустой список, для включения в него найденных на странице групп
            for element in wd.find_elements_by_css_selector("span.group"):  # Для каждой группы со страницы берем id и name и помещаем в список
               text = element.text
               id = element.find_element_by_name("selected[]").get_attribute("value")
               self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)  # возвращаем копию полученного списка групп
# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

## Precondition
def create_contact_if_contact_list_empty(app):  # Предусловие првоеряет наличие хотя бы одного контакта, которого можно изменить. Если такого контакта нет, то создаем.
    if app.contact.count() == 0:
        app.contact.create(Contact("my name", "my middlename ", "my lastname", "my nickname", "my title", "my company", "my adress", "my telephone", "my home", "my mobile", "my work", "my fax", "my email2", "my email3", "1", "February", "2000", "3", "February",
                            "2012", "qwqw", "qwqw", "qwqw"))


## Tests
def test_edit_rundom_contact(app):
    create_contact_if_contact_list_empty(app)  # Проверяем, есть ли на главной странице - контакты, которые можно изменить, если их нет, то создаем контакт
    old_contacts = app.contact.get_contact_list()  # Оракул. получаем список контактов на странице до выполнения действия
    index = randrange(len(old_contacts))  # выбираем произвольный index контакта из списка контактов собранных со страницы.
    contact = Contact(firstname="new firstname", middlename="new middlename", lastname="new lastname")
    contact.id = old_contacts[index].id
    app.contact.edit_by_index(contact, index)  # выполняем действие редактирования контакта
    assert len(old_contacts) == app.contact.count()   # Проверяем, что после выполнения действия кол-во контактов на странице не изменилось
    new_contacts = app.contact.get_contact_list()  # Получаем список контактов со страницы, после выполнения действия
    old_contacts[index] = contact  # Оракул. Изменяем в оракуле данные отредактированного через интерфейс контакта
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


'''
def test_edit_contact_name_section(app):
    create_contact_if_contact_list_empty(app)
    app.contact.edit_first_contact(Contact(firstname="new firstname", middlename="new middlename", lastname="new lastname"))
'''
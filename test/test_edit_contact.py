# -*- coding: utf-8 -*-
from model.contact import Contact
import random

## Precondition
def create_contact_if_contact_list_empty(app, db):  # Предусловие првоеряет наличие хотя бы одного контакта, которого можно изменить. Если такого контакта нет, то создаем.
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("my name", "my middlename ", "my lastname", "my nickname", "my title", "my company", "my adress", "my telephone", "my home", "my mobile", "my work", "my fax", "my email2", "my email3", "1", "February", "2000", "3", "February",
                            "2012", "qwqw", "qwqw", "qwqw"))


## Tests
def test_edit_random_contact(app, db, check_ui):
    create_contact_if_contact_list_empty(app, db)  # Проверяем, есть ли на главной странице - контакты, которые можно изменить, если их нет, то создаем контакт
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    new_contact_data = Contact(firstname="new firstname", middlename="new middlename", lastname="new lastname")
    new_contact_data.id = old_contacts[index].id
    app.contact.edit_by_id(new_contact_data, contact.id)  # выполняем действие редактирования контакта
    new_contacts = db.get_contact_list()  # Получаем список контактов со страницы, после выполнения действия
    old_contacts[index] = new_contact_data  # Оракул. Изменяем в оракуле данные отредактированного через интерфейс контакта
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)

'''
def test_edit_contact_name_section(app):
    create_contact_if_contact_list_empty(app)
    app.contact.edit_first_contact(Contact(firstname="new firstname", middlename="new middlename", lastname="new lastname"))
'''
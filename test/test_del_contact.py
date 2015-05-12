# -*- coding: utf-8 -*-
from model.contact import Contact
import random

# Precondition
def create_contact_if_contact_list_empty(app, db):  # Предусловие првоеряет наличие хотя бы одного контакта, которого можно удалить. Если такого контакта нет, то создаем.
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="contact for delete"))


# Tests
def test_delete_random_contact_from_main_page(app, db, check_ui):
    create_contact_if_contact_list_empty(app, db)  # Проверяем, есть ли на главной странице - контакты, которые можно удалить, если их нет, то создаем контакт
    old_contacts = db.get_contact_list()  # Оракул. получаем список контактов до выполнения действия
    contact = random.choice(old_contacts)
    app.contact.delete_by_id_from_main_page(contact.id)  # выполняем действие удаления контакта
    app.go_to_home_page()
    new_contacts = db.get_contact_list()  # Получаем список контактов со страницы, после выполнения действия
    old_contacts.remove(contact)  # Оракул. Удаляем из оракула удаленный через интерфейс контакт
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)


def test_delete_random_contact_from_contact_form(app, db, check_ui):
    create_contact_if_contact_list_empty(app, db)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id_from_contact_form(contact.id)
    app.go_to_home_page()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)

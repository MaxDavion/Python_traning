# -*- coding: utf-8 -*-
from model.contact import Contact

# Precondition
def create_contact_if_contact_list_empty(app):  # Создаем контакт, если нечего удалять
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="contact for delete"))


# Tests
def test_delite_contact_from_main_page(app):
    create_contact_if_contact_list_empty(app)
    old_contacts = app.contact.get_contact_list()  # оракул. получаем список контактов на странице до выполнения действия
    app.contact.delete_from_main_page()  # выполняем удаление первого контакта на странице
    new_contacts = app.contact.get_contact_list()  # получаем список контактов на странице после выполнения действия
    assert len(old_contacts) - 1 == len(new_contacts)  # Проверяем что кол-во контактов на странице уменьшилось на 1
    old_contacts[0:1] = []  # Удаляем из оракула первый контакт
    assert sorted(old_contacts, key=lambda contact: int(contact.id)) == sorted(new_contacts, key=lambda contact: int(contact.id))


def test_delite_contact_from_contact_form(app):
    create_contact_if_contact_list_empty(app)
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_from_contact_form()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert sorted(old_contacts, key=lambda contact: int(contact.id)) == sorted(new_contacts, key=lambda contact: int(contact.id))

# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact


# ТЕСТ
# json_groups - берем данные из data\group.json
# data_groups - берем данные из data\groups.py
def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()  # Оракул. Получаем список контактов из базы, до выполнения действия
    app.contact.create(contact)  # Выполняем действие создания контакта
    new_contacts = db.get_contact_list()  # Получаем список групп со из базы, после выполнения действия
    old_contacts.append(contact)  # Оракул. Добавляем в оракула созданный через интерфейс контакт
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)  # Проверить, что добавленый контакт присутствует на странице




# BACKUP
'''
# ТЕСТ
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()  # Оракул. Получаем список контактов со страницы, до выполнения действия
    app.contact.create(contact)  # Выполняем действие создания контакта
    assert len(old_contacts) + 1 == app.contact.count()  # Проверяем, что после выполнения действия кол-во контактов на странице увеличилось на 1
    new_contacts = app.contact.get_contact_list()  # Получаем список групп со страницы, после выполнения действия
    old_contacts.append(contact)  # Оракул. Добавляем в оракула созданный через интерфейс контакт
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)  # Проверить, что добавленый контакт присутствует на странице
'''
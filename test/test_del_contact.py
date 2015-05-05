# -*- coding: utf-8 -*-
from model.contact import Contact
import random

# Precondition
def create_contact_if_contact_list_empty(app, db):  # Предусловие првоеряет наличие хотя бы одного контакта, которого можно удалить. Если такого контакта нет, то создаем.
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="contact for delete"))


# Tests
def test_delete_random_contact_from_main_page(app, db):
    # create_contact_if_contact_list_empty(app, db)  # Проверяем, есть ли на главной странице - контакты, которые можно удалить, если их нет, то создаем контакт
    old_contacts = db.get_contact_list()  # Оракул. получаем список контактов до выполнения действия
    print(old_contacts)
    contact = random.choice(old_contacts)
    app.contact.delete_by_id_from_main_page(contact.id)  # выполняем действие удаления контакта
    old_contacts.remove(contact)  # Оракул. Удаляем из оракула удаленный через интерфейс контакт
    print(old_contacts)
    new_contacts = db.get_contact_list()  # Получаем список контактов со страницы, после выполнения действия
    print(new_contacts)

    assert sorted(old_contacts, key=lambda contact: int(contact.id)) == sorted(new_contacts, key=lambda contact: int(contact.id))  # Проверить, что удаленный контакт отсутствует на странице, а остальные контакты присутствуют

'''
def test_delete_random_contact_from_contact_form(app):
    create_contact_if_contact_list_empty(app)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index_from_contact_form(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=lambda contact: int(contact.id)) == sorted(new_contacts, key=lambda contact: int(contact.id))
'''
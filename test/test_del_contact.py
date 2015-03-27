# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

# Precondition
def create_contact_if_contact_list_empty(app):  # Предусловие првоеряет наличие хотя бы одного контакта, которого можно удалить. Если такого контакта нет, то создаем.
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="contact for delete"))


# Tests
def test_delete_random_contact_from_main_page(app):
    create_contact_if_contact_list_empty(app)  # Проверяем, есть ли на главной странице - контакты, которые можно удалить, если их нет, то создаем контакт
    old_contacts = app.contact.get_contact_list()  # Оракул. получаем список контактов на странице до выполнения действия
    index = randrange(len(old_contacts))  # выбираем произвольный index контакта из списка контактов собранных со страницы.
    app.contact.delete_by_index_from_main_page(index)  # выполняем действие удаления контакта
    assert len(old_contacts) - 1 == app.contact.count()  # Проверяем, что после выполнения действия кол-во контактов на странице уменьшилось на 1
    new_contacts = app.contact.get_contact_list()  # Получаем список контактов со страницы, после выполнения действия
    old_contacts[index:index+1] = []  # Оракул. Удаляем из оракула удаленный через интерфейс контакт
    assert sorted(old_contacts, key=lambda contact: int(contact.id)) == sorted(new_contacts, key=lambda contact: int(contact.id))  # Проверить, что удаленный контакт отсутствует на странице, а остальные контакты присутствуют


def test_delete_random_contact_from_contact_form(app):
    create_contact_if_contact_list_empty(app)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index_from_contact_form(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=lambda contact: int(contact.id)) == sorted(new_contacts, key=lambda contact: int(contact.id))

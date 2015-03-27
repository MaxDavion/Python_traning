# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()  # Оракул. Получаем список контактов со страницы, до выполнения действия
    contact = Contact("my name", "my middlename ", "my lastname", "my nickname", "my title", "my company", "my adress", "my telephone", "my home", "my mobile", "my work", "my fax", "my email2", "my email3", "1", "February", "2000", "3", "February",
                            "2012", "qwqw", "qwqw", "qwqw")
    app.contact.create(contact)  # Выполняем действие создания контакта
    assert len(old_contacts) + 1 == app.contact.count()  # Проверяем, что после выполнения действия кол-во контактов на странице увеличилось на 1
    new_contacts = app.contact.get_contact_list()  # Получаем список групп со страницы, после выполнения действия
    old_contacts.append(contact)  # Оракул. Добавляем в оракула созданный через интерфейс контакт
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)  # Проверить, что добавленый контакт присутствует на странице

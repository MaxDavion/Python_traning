# -*- coding: utf-8 -*-
import pytest
import string
import random
from model.contact import Contact
import re

# МЕТОДЫ ГЕНЕРАЦИИ РАНДОМНЫХ ДАННЫХ

# Метод возвращает строку(не длиннее чем maxlen с префиксом + сучайно сгенерированными символами (буквы + числа))
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*8
    return clear_random_string(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).rstrip())

# Метод возвращает номер телефона(не длиннее чем maxlen со сучайно сгенерированными числами)
def random_phone(maxlen):
    symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return "+" + random.choice(symbols) + " " + "".join([random.choice(symbols) for i in range(maxlen)]).rstrip()

# Метод возвращает e-mail(со сучайно сгенерированными символами)
def random_email(maxlenlogin, maxlendomen):
    symbols = string.ascii_letters + string.digits + "_"*3 + "-"*3 + "."*3
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlenlogin))]) + "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlendomen))]) + "." + "".join([random.choice(symbols) for i in range(2, 3)])

# Метод возвращает случайно выбранный месяц
def random_month():
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    index = random.randrange(len(month))
    return month[index]

# Метод возвращает число в виде строки (число не больше чем max)
def random_digits(max):
    return str(random.randrange(max))

# Метод, случайным образом определяющий, нужно перезаписывать то что автоматически проставляется в поле e-mail.
def random_override_avtogenerate_email():
    symbols = "Y" + "N"
    if random.choice(symbols) == "Y":
        return None
    else:
        return random_email(10, 10)

def clear_random_string(str):
    return re.sub(r'\s+', ' ', str)


# ТЕСТОВЫЕ ДАННЫЕ
testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname=random_string("firstname", 20), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20), nickname=random_string("nickname", 15),
            title=random_string("title", 15), company=random_string("company", 15), address=random_string("address", 25), homepage=random_string("homepage", 25),
            home=random_phone(9), mobile=random_phone(9), work=random_phone(9), fax=random_phone(9), phone_secondary=random_phone(9),
            email=random_override_avtogenerate_email(), email2=random_email(10, 10), email3=random_email(10, 10),
            bday=random_digits(31), bmonth=random_month(), byear=random_digits(9999), aday=random_digits(31), amonth=random_month(), ayear=random_digits(9999),
            address_secondary=random_string("address_secondary", 25), notes=random_string("notes", 25))
    for i in range(5)
]


# ТЕСТ
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()  # Оракул. Получаем список контактов со страницы, до выполнения действия
    app.contact.create(contact)  # Выполняем действие создания контакта
    assert len(old_contacts) + 1 == app.contact.count()  # Проверяем, что после выполнения действия кол-во контактов на странице увеличилось на 1
    new_contacts = app.contact.get_contact_list()  # Получаем список групп со страницы, после выполнения действия
    old_contacts.append(contact)  # Оракул. Добавляем в оракула созданный через интерфейс контакт
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)  # Проверить, что добавленый контакт присутствует на странице

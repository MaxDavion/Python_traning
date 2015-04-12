# -*- coding: utf-8 -*-
from model.contact import Contact
import generator_helper

# ФАЙЛ ГЕНЕРАЦИИ ГРУПП
# Файл может быть запущен с параметрами:  -n XX -f YYYY (где XX - кол-во контактов, YYYY - путь к файлу относительно папки проекта + название файла)
# Пример запуска с коммандной строки: contact.py -n 5 -f /data/test.json


# Параметры генерации данных в .json файл по умолчанию
n = 5  # кол-во генерируемых контактов
out_file = "/data/contacts.json"  # в какой файл генерировать

# Првоеряем, задавались ли параметры генерации с командной строки. если задавались то используем их, если не задавались - то используем по умолчанию
if generator_helper.read_from_command_line().number:
    n = int(generator_helper.read_from_command_line().number)
if generator_helper.read_from_command_line().file:
    out_file = generator_helper.read_from_command_line().file

# Генерируем нужное кол-во групп с рандомными атрибутами
testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname=generator_helper.random_string("firstname", 20), middlename=generator_helper.random_string("middlename", 20), lastname=generator_helper.random_string("lastname", 20), nickname=generator_helper.random_string("nickname", 15),
            title=generator_helper.random_string("title", 15), company=generator_helper.random_string("company", 15), address=generator_helper.random_string("address", 25), homepage=generator_helper.random_string("homepage", 25),
            home=generator_helper.random_phone(9), mobile=generator_helper.random_phone(9), work=generator_helper.random_phone(9), fax=generator_helper.random_phone(9), phone_secondary=generator_helper.random_phone(9),
            email=generator_helper.random_override_avtogenerate_email(), email2=generator_helper.random_email(10, 10), email3=generator_helper.random_email(10, 10),
            bday=generator_helper.random_digits(31), bmonth=generator_helper.random_month(), byear=generator_helper.random_digits(9999), aday=generator_helper.random_digits(31), amonth=generator_helper.random_month(), ayear=generator_helper.random_digits(9999),
            address_secondary=generator_helper.random_string("address_secondary", 25), notes=generator_helper.random_string("notes", 25))
    for i in range(n)
]

#  Записываем сгенерированные данные в файл-json
generator_helper.write_testdata_to_json_file(testdata, out_file)


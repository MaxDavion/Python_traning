# -*- coding: utf-8 -*-
import string
import random
import os.path
import jsonpickle
import re
import argparse


# Метод чтения параметров запуска генерации с командной строки. Если параметры заданы, то они будут возвращены.
# Формат команды -n XX -f YYYY (где XX - кол-во групп, YYYY - путь к файлу относительно папки проекта + название файла)
def read_from_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', action='store', dest='number', help='number of Groups')
    parser.add_argument('-f', action='store', dest='file', help='file')
    return parser.parse_args()


# Метод записывае в json файл переданные ему данные
def write_testdata_to_json_file(testdata, out_file):
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".." + out_file)
    with open(file, "w") as out:
        jsonpickle.set_encoder_options("json", indent=2)
        out.write(jsonpickle.encode(testdata))
        print("Complete")


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

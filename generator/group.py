# -*- coding: utf-8 -*-
from model.group import Group
import generator_helper

# ФАЙЛ ГЕНЕРАЦИИ ГРУПП
# Файл может быть запущен с параметрами:  -n XX -f YYYY (где XX - кол-во групп, YYYY - путь к файлу относительно папки проекта + название файла)
# Пример запуска с коммандной строки: group.py -n 5 -f /data/test.json


# Параметры генерации данных в .json файл по умолчанию
n = 5  # кол-во генерируемых групп
out_file = "/data/groups.json"  # в какой файл генерировать

# Првоеряем, задавались ли параметры генерации с командной строки. если задавались то используем их, если не задавались - то используем по умолчанию
if generator_helper.read_from_command_line().number:
    n = int(generator_helper.read_from_command_line().number)
if generator_helper.read_from_command_line().file:
    out_file = generator_helper.read_from_command_line().file

# Генерируем нужное кол-во групп с рандомными атрибутами
testdata = [Group(name="", header="", footer="")] + [
    Group(name=generator_helper.random_string("name", 10), header=generator_helper.random_string("header", 20), footer=generator_helper.random_string("footer", 20))
    for i in range(n)
]

#  Записываем сгенерированные данные в файл-json
generator_helper.write_testdata_to_json_file(testdata, out_file)



# BACKUP
'''
# Работа через модуль json

import json
# Метод записывает тестовые данные в json.file (даныне из файла testdata)
with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
'''
# -*- coding: utf-8 -*-

from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    # Изменяем  вид вывода объекта на консоль
    def __repr__(self):
        return '%s:%s:%s:%s' % (self.id, self.name, self.header, self.footer)

    # Перегрузка функции сравнения, для сравнения списка групп
    def __eq__(self, other):
        return self.name == other.name and (self.id is None or other.id is None or self.id == other.id)

    # Метод, возвращающий  id группы если он есть или большое число, если у группы еще нет idю Используется как ключ в проверке списков групп
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize





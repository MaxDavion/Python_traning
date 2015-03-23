# -*- coding: utf-8 -*-

class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    ##Изменяем  вид вывода объекта на консоль
    def __repr__(self):
        return '%s:%s' % (self.id, self.name)

    ##Перегрузка функции сравнения, для сравнения списка групп
    def __eq__(self, other):
        return self.name == other.name and self.id == other.id





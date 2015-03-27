# -*- coding: utf-8 -*-
from model.group import Group
from random import  randrange

## Precondition
def create_group_if_group_list_empty(app):  # Предусловие првоеряет наличие хотя бы одной группы, которую можно редакировать. Если такой группы нет, то создаем.
    if app.group.count() == 0:
        app.group.create(Group(name="groupname", header="groupheader", footer="groupfooter"))


##Tests
def test_edit_random_group(app):
    create_group_if_group_list_empty(app)  # Проверяем, есть ли на странице групп - группы, которые можно изменить, если их нет, то создаем группу
    group = Group(name="newgroupname", header="newgroupheader", footer="newgroupfooter")
    old_group = app.group.get_group_list()  # Оракул. Получаем список групп со страницы, до выполнения действия
    index = randrange(len(old_group))  # выбираем произвольный index группы из списка групп собранных со страницы.
    group.id = old_group[index].id
    app.group.edit_by_index(group, index)  # Выполняем действие редактирования группы
    assert len(old_group) == app.group.count()  # Проверяем, что после выполнения действия кол-во групп на странице не изменилось
    new_group = app.group.get_group_list()  # Получаем список групп со страницы, после выполнения действия
    old_group[index] = group  # Оракул. Изменяем в оракуле данные отредактированной через интерфейс группы
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)


'''
def test_edit_group_name(app):
    create_group_if_group_list_empty(app)
    old_group = app.group.get_group_list()
    app.group.edit(Group(name="new name"))
    new_group = app.group.get_group_list()
    assert len(old_group) == len(new_group)

def test_edit_group_header(app):
    create_group_if_group_list_empty(app)
    old_group = app.group.get_group_list()
    app.group.edit(Group(header="new header"))
    new_group = app.group.get_group_list()
    assert len(old_group) == len(new_group)

def test_edit_group_footer(app):
    create_group_if_group_list_empty(app)
    old_group = app.group.get_group_list()
    app.group.edit(Group(footer="new footer"))
    new_group = app.group.get_group_list()
    assert len(old_group) == len(new_group)
'''


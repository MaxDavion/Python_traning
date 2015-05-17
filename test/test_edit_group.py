# -*- coding: utf-8 -*-
from model.group import Group
import random

## Precondition
def create_group_if_group_list_empty(app, db):  # Предусловие првоеряет наличие хотя бы одной группы, которую можно редакировать. Если такой группы нет, то создаем.
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="groupname", header="groupheader", footer="groupfooter"))

'''
##Tests
def test_edit_random_group(app, db, check_ui):
    create_group_if_group_list_empty(app, db)  # Проверяем, есть ли на странице групп - группы, которые можно изменить, если их нет, то создаем группу
    new_group_data = Group(name="newgroupname", header="newgroupheader", footer="newgroupfooter")
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    new_group_data.id = old_groups[index].id
    app.group.edit_by_id(new_group_data, group.id)  # Выполняем действие редактирования группы
    new_groups = db.get_group_list()
    old_groups[index] = new_group_data  # Оракул. Изменяем в оракуле данные отредактированной через интерфейс группы
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(db.get_group_list(), key=Group.id_or_max)
'''

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
'''

def test_edit_group_footer(app):
    create_group_if_group_list_empty(app)
    old_group = app.group.get_group_list()
    app.group.edit(Group(footer="new footer"))
    new_group = app.group.get_group_list()
    assert len(old_group) == len(new_group)



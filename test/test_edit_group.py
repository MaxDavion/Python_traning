# -*- coding: utf-8 -*-
from model.group import Group


## Precondition
def create_group_if_group_list_empty(app):
    if app.group.count() == 0:
        app.group.create(Group(name="groupname", header="groupheader", footer="groupfooter"))


##Tests
def test_edit_group(app):
    create_group_if_group_list_empty(app)
    old_group = app.group.get_group_list()
    app.group.edit(Group(name="newgroupname", header="newgroupheader", footer="newgroupfooter"))
    new_group = app.group.get_group_list()
    ## Проверить, что после редактирования кол-во групп не изменилось
    assert len(old_group) == len(new_group)


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



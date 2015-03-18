# -*- coding: utf-8 -*-
from model.group import Group


## Precondition
def create_group_if_group_list_empty(app):
    if app.group.count() == 0:
        app.group.create(Group(name="groupname", header="groupheader", footer="groupfooter"))


##Tests
def test_edit_group(app):
    create_group_if_group_list_empty(app)
    app.group.edit(Group(name="newgroupname", header="newgroupheader", footer="newgroupfooter"))

def test_edit_group_name(app):
    create_group_if_group_list_empty(app)
    app.group.edit(Group(name="new name"))

def test_edit_group_header(app):
    create_group_if_group_list_empty(app)
    app.group.edit(Group(header="new header"))

def test_edit_group_footer(app):
    create_group_if_group_list_empty(app)
    app.group.edit(Group(footer="new footer"))



# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group(app):
    app.session.login(user="admin", password="secret")
    app.group.edit(Group(name="newgroupname", header="newgroupheader", footer="newgroupfooter"))
    app.session.logout()

def test_edit_group_name(app):
    app.session.login(user="admin", password="secret")
    app.group.edit(Group(name="new name"))
    app.session.logout()

def test_edit_group_header(app):
    app.session.login(user="admin", password="secret")
    app.group.edit(Group(header="new header"))
    app.session.logout()

def test_edit_group_footer(app):
    app.session.login(user="admin", password="secret")
    app.group.edit(Group(footer="new footer"))
    app.session.logout()


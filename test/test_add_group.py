# -*- coding: utf-8 -*-
from model.group import Group

def test_create_group(app):
    app.group.create(Group("groupname", "groupheader", "groupfooter"))
    app.session.logout()

def test_create_empty_group(app):
    app.group.create(Group("", "", ""))



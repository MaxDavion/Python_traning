# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group(app):
    app.session.login(user="admin", password="secret")
    app.group.edit(Group("newgroupname", "newgroupheader", "newgroupfooter"))
    app.session.logout()



# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_group(app):
    app.login(user="admin", password="secret")
    app.create_group(Group("groupname", "groupheader", "groupfooter"))
    app.logout()

def test_create_empty_group(app):
    app.login(user="admin", password="secret")
    app.create_group(Group("", "", ""))
    app.logout()



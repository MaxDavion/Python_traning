# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(user="admin", password="secret")
    app.contact.create(Contact("my name", "my middlename ", "my lastname", "my nickname", "my title", "my company", "my adress", "my telephone", "my home", "my mobile", "my work", "my fax", "my email2", "my email3", "1", "February", "2000", "3", "February",
                            "2012", "qwqw", "qwqw", "qwqw"))
    app.session.logout()

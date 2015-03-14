# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact("my name", "my middlename ", "my lastname", "my nickname", "my title", "my company", "my adress", "my telephone", "my home", "my mobile", "my work", "my fax", "my email2", "my email3", "1", "February", "2000", "3", "February",
                            "2012", "qwqw", "qwqw", "qwqw"))

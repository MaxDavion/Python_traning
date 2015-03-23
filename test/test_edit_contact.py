# -*- coding: utf-8 -*-
from model.contact import Contact

## Precondition
def create_contact_if_contact_list_empty(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("my name", "my middlename ", "my lastname", "my nickname", "my title", "my company", "my adress", "my telephone", "my home", "my mobile", "my work", "my fax", "my email2", "my email3", "1", "February", "2000", "3", "February",
                            "2012", "qwqw", "qwqw", "qwqw"))


## Tests
def test_edit_contact(app):
    create_contact_if_contact_list_empty(app)
    app.contact.edit(Contact("new name", "new middlename", "new lastname", "new nickname", "new title", "new company", "new adress", "new telephone", "new home", "new mobile", "new work", "new fax", "new email2", "new email3", "5", "February", "2009", "7", "February",
                            "2011", "new", "new", "new"))

def test_edit_contact_name_section(app):
    create_contact_if_contact_list_empty(app)
    app.contact.edit(Contact(firstname="new firstname", middlename="new middlename", lastname="new lastname"))

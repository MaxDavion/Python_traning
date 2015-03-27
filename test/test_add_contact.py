# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact("my name", "my middlename ", "my lastname", "my nickname", "my title", "my company", "my adress", "my telephone", "my home", "my mobile", "my work", "my fax", "my email2", "my email3", "1", "February", "2000", "3", "February",
                            "2012", "qwqw", "qwqw", "qwqw")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)

from model.group import Group
from model.contact import Contact
import mysql.connector

'''
def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_list = map(lambda group: Group(id=group.id, name=group.name.strip()), db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
'''

def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    db_list = map(lambda contact: Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(), address=contact.address.strip(), all_phones_from_home_page=contact.all_phones_from_home_page.strip(), all_emails_from_home_page=contact.all_emails_from_home_page.strip()), db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)







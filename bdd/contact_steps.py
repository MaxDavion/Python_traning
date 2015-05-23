from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given('a contact with <firstname>, <lastname>, <address>')
def new_contact(firstname, lastname, address):
    return Contact(firstname=firstname, lastname=lastname, address=address)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)

@then('the new contact list is equal to the old list with added contact')
def verify_contact_added(contact_list, new_contact, db):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)

@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="contact for delete"))
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_by_id_from_main_page(random_contact.id)
    app.go_to_home_page()

@then('the new contact list is equal to the old list without deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)

@when('I edit the contact from the list')
def edit_contact(app, random_contact, new_contact):
    app.contact.edit_by_id(new_contact, random_contact.id)

@then('the new contact list is equal to the old list with edit contact')
def verify_contact_deleted(db, random_contact, non_empty_contact_list, new_contact):
    old_contacts = non_empty_contact_list
    index = old_contacts.index(random_contact)
    old_contacts[index] = new_contact
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
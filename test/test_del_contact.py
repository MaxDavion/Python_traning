from model.contact import Contact

## Precondition
def create_contact_if_contact_list_empty(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="contact for delete"))


## Tests
def test_delite_contact_from_main_page(app):
    create_contact_if_contact_list_empty(app)
    app.contact.delete_from_main_page()

def test_delite_contact_from_contact_form(app):
    create_contact_if_contact_list_empty(app)
    app.contact.delete_from_contact_form()



def test_delite_contact_from_main_page(app):
    app.contact.delete_from_main_page()

def test_delite_contact_from_contact_form(app):
    app.contact.delete_from_contact_form()
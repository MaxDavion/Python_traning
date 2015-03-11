

def test_delite_contact_from_main_page(app):
    app.session.login(user="admin", password="secret")
    app.contact.delete_from_main_page()
    app.session.logout()

def test_delite_contact_from_contact_form(app):
    app.session.login(user="admin", password="secret")
    app.contact.delete_from_contact_form()
    app.session.logout()


def test_delite_contact(app):
    app.session.login(user="admin", password="secret")
    app.contact.delete()
    app.session.logout()
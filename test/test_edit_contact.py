from model.contact import Contact


def test_edit_contact(app):
    app.session.login(user="admin", password="secret")
    app.contact.edit(Contact("new name", "new middlename", "new lastname", "new nickname", "new title", "new company", "new adress", "new telephone", "new home", "new mobile", "new work", "new fax", "new email2", "new email3", "5", "February", "2009", "7", "February",
                            "2011", "new", "new", "new"))
    app.session.logout()

def test_edit_contact_name_section(app):
    app.session.login(user="admin", password="secret")
    app.contact.edit(Contact(firstname="new firstname", middlename="new middlename", lastname="new lastname"))
    app.session.logout()

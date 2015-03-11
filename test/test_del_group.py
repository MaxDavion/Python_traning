

def test_delite_group(app):
    app.session.login(user="admin", password="secret")
    app.group.delete_from_main_page()
    app.session.logout()
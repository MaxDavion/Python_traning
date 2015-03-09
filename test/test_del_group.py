

def test_delite_group(app):
    app.session.login(user="admin", password="secret")
    app.group.delete()
    app.session.logout()
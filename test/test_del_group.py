from model.group import Group

def test_delite_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group for delete"))
    app.group.delete()
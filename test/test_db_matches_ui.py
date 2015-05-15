from model.group import Group
import mysql.connector


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_list = map(lambda group: Group(id=group.id, name=group.name.strip()), db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


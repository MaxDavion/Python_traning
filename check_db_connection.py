import mysql.connector
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="localhost", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id='60'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass



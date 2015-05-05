import mysql.connector
from fixture.orm import ORMFixture

db = ORMFixture(host="localhost", name="addressbook", user="root", password="")

try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass



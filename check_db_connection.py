import mysql.connector
from model.group import Group

# connection = mysql.connector.Connect(host="192.168.0.100", port='3306', database="addressbook", user="root", password="")
connection = mysql.connector.Connect(host="localhost", port='3306', database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    list = []
    cursor.execute("select id from addressbook where deprecated = '0000-00-00 00:00:00'")
    for row in cursor:
        (id) = row
        list.append(Group(id=id))
    print(list)
finally:
    connection.close



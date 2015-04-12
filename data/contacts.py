# -*- coding: utf-8 -*-
from model.contact import Contact

# ТЕСТОВЫЕ ДАННЫЕ
testdata = [
    Contact(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
            title="title", company="company", address="address", homepage="homepage",
            home="78880000000", mobile="78880000001", work="78880000002", fax="78880000003", phone_secondary="78880000004",
            email="email@mail.com", email2="email2@mail.com", email3="email3@mail.com",
            bday="11", bmonth="May", byear="2015", aday="11", amonth="May", ayear="2015",
            address_secondary="address_secondary", notes="notes"),
    Contact(firstname="", middlename="", lastname="")
           ]

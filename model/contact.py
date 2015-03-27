# -*- coding: utf-8 -*-
from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home=None, mobile=None, work=None, fax=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, address_secondary=None, phone_secondary=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address_secondary = address_secondary
        self.phone_secondary = phone_secondary
        self.notes = notes
        self.id = id

    def __repr__(self):
        return '%s:%s' % (self.id, self.lastname)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and self.lastname == other.lastname

    # Метод, возвращающий  id группы если он есть или большое число, если у группы еще нет idю Используется как ключ в проверке списков групп
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

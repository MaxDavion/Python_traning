# -*- coding: utf-8 -*-
import re
from random import randrange
from model.contact import Contact


# Вспомогательная функция. Чистит номера телефонов, убирая из них знаки указанные в регулярном выражении
def clear(s):
    return re.sub("[() -]","", s)

# Вспомогательный метод реализующий обратные проверки для номеров телефоно. Из полученного списка(объекта Контакт) берет номера телефонов и склеивает их, т.к на главной странице
def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                              map(lambda x: clear(x),
                                  filter(lambda x: x is not None,
                                         [contact.home, contact.mobile, contact.work, contact.phone_secondary]))))

# Вспомогательный метод реализующий обратные проверки для e-mail. Из полученного списка(объекта Контакт) берет e-mail и склеивает их, т.к на главной странице
def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                          filter(lambda x: x is not None,
                                 [contact.email, contact.email2, contact.email3])))


#ТЕСТЫ

#  Для случайно выбранного контакта информация на главной странице соответствует информации, представленной в форме редактирования контакта
def test_all_contact_data_from_home_page_equal_contact_data_from_edit_page(app):
    index = randrange(app.contact.count())  # выбираем произвольный index контакта из списка контактов собранных со страницы.
    contact_from_home_page = app.contact.get_contact_list()[index]  # Получае данные с главной страницы по выбранному контакту
    app.contact.open_contact_to_edit_by_index(index)  # Открываем на редактирование выбранный контакт
    contact_from_edit_page = app.contact.get_contact_details_from_edit_page()  # Получаем данные со страницы редактирования выбранного контакта
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname # Здесь и ниже сравниваем данные
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails(contact_from_edit_page)



'''
def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    app.contact.open_contact_to_edit_by_index(0)
    contact_from_edit_page = app.contact.get_contact_details_from_edit_page()
    assert contact_from_home_page.all_phones_from_home_page == merge_phones(contact_from_edit_page)
'''

'''
def test_phones_on_contact_details_page(app):
    app.contact.open_contact_to_edit_by_index(0)
    contact_from_edit_page = app.contact.get_contact_details_from_edit_page()
    app.contact.open_contact_to_view_by_index(0)
    contact_from_view_page = app.contact.get_contact_details_from_view_page()
    assert contact_from_edit_page.home == contact_from_view_page.home
    assert contact_from_edit_page.mobile == contact_from_view_page.mobile
    assert contact_from_edit_page.work == contact_from_view_page.work
    assert contact_from_edit_page.phone_secondary == contact_from_view_page.phone_secondary
'''



# -*- coding: utf-8 -*-
from pytest_bdd import given, when, then
from model.group import Group
import random
import pytest

@given('a group list')
def group_list(db):
    with pytest.allure.step('Given a group list'):
        return db.get_group_list()


@given('a group with <name>, <header>, <footer>')
def new_group(name, header, footer):
    with pytest.allure.step('Given a group with name={name}, header={header} and footer={footer}'):
        return Group(name=name, header=header, footer=footer)

@when('I add the group to the list')
def add_new_group(app, new_group):
    with pytest.allure.step('When I add the group to the list'):  # Помечаем участок кода как шаг
        app.group.create(new_group)

@then('the new group list is equal to the old list with added group')
def verify_group_added(db, group_list, new_group):
    with pytest.allure.step('Then the new group list is equal to the old list with added group'):
        old_groups = group_list
        new_groups = db.get_group_list()
        old_groups.append(new_group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@given('a non-empty group list')
def non_empty_group_list(db, app):
    with pytest.allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="group for delete"))
        return db.get_group_list()

pytest.allure.step('Given a random group from the list')
@given('a random group from the list')
def random_group(non_empty_group_list):
    with pytest.allure.step('Given a random group from the list'):
        return random.choice(non_empty_group_list)

@when('I delete the group from the list')
def delete_group(app, random_group):
    with pytest.allure.step('When I delete the group %s from the list' % random_group):
        app.group.delete_by_id(random_group.id)

@then('the new group list is equal to the old list without deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group):
    with pytest.allure.step('Then the new group list is equal to the old list without deleted group'):
        old_groups = non_empty_group_list
        new_groups = db.get_group_list()
        old_groups.remove(random_group)
        assert old_groups == new_groups
        assert sorted(new_groups, key=Group.id_or_max) == sorted(db.get_group_list(), key=Group.id_or_max)

@when('I edit the group from the list')
def edit_group(app, random_group, new_group):
    with pytest.allure.step('When I edit the group %s from the list' % random_group):
        app.group.edit_by_id(new_group, random_group.id)

@then('the new group list is equal to the old list with edit group')
def verify_group_deleted(db, random_group, non_empty_group_list, new_group):
    with pytest.allure.step('Then the new group list is equal to the old list with edit group'):
        old_groups = non_empty_group_list
        index = old_groups.index(random_group)
        old_groups[index] = new_group
        new_groups = db.get_group_list()
        assert old_groups == new_groups
        assert sorted(new_groups, key=Group.id_or_max) == sorted(db.get_group_list(), key=Group.id_or_max)






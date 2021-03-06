# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import allure

# ТЕСТ
# json_groups - берем данные из data\group.json
# data_groups - берем данные из data\groups.py
@allure.feature('Feature1')
@allure.story('Story1')
def test_create_group(app, db, json_groups):
    group = json_groups
    with pytest.allure.step('Запоминаем список групп на странице'):
        old_groups = db.get_group_list()
    with pytest.allure.step('Добавляем новую группу'):
        app.group.create(group)
    with pytest.allure.step('Проверяем что новая группа добавлена'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# BACKUP
'''''
import pytest
from data.groups import constant as testdata

# ТЕСТ
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_create_empty_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    '''




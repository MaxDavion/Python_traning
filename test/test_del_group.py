# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest



def test_delete_random_group(app, db, check_ui):
    with pytest.allure.step('Предусловие: Проверяем, есть ли на странице групп - группы, которые можно удалить, если их нет, то создаем группу'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="group for delete"))
    with pytest.allure.step('Оракул. Получаем список групп, до выполнения действия'):
        old_groups = db.get_group_list()
    with pytest.allure.step('Выполняем действие удаления случайной группы'):
        group = random.choice(old_groups)
        app.group.delete_by_id(group.id)  #
    with pytest.allure.step('Проверяему что группа удалена'):
        new_groups = db.get_group_list()  #
        old_groups.remove(group)  # Оракул. Удаляем из оракула удаленную через интерфейс группу
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(db.get_group_list(), key=Group.id_or_max)
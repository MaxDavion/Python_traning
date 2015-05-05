# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_delete_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:  # Проверяем, есть ли на странице групп - группы, которые можно удалить, если их нет, то создаем группу
        app.group.create(Group(name="group for delete"))
    old_groups = db.get_group_list()  # Оракул. Получаем список групп, до выполнения действия
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)  # Выполняем действие удаления группы
    new_groups = db.get_group_list()  # Получаем список групп, после выполнения действия
    old_groups.remove(group)  # Оракул. Удаляем из оракула удаленную через интерфейс группу
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=lambda group: int(group.id)) == sorted(app.group.get_group_list(), key=lambda group: int(group.id))
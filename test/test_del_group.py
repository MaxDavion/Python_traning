# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_delete_random_group(app):
    if app.group.count() == 0:  # Проверяем, есть ли на странице групп - группы, которые можно удалить, если их нет, то создаем группу
        app.group.create(Group(name="group for delete"))
    old_groups = app.group.get_group_list()  # Оракул. Получаем список групп со страницы, до выполнения действия
    index = randrange(len(old_groups))  # выбираем произвольный index группы из списка групп собранных со страницы.
    app.group.delete_by_index(index)  # Выполняем действие удаления группы
    assert len(old_groups) - 1 == app.group.count()  # Проверяем, что после выполнения действия кол-во групп на странице уменьшилось на 1
    new_groups = app.group.get_group_list()  # Получаем список групп со страницы, после выполнения действия
    old_groups[index:index+1] = []  # Оракул. Удаляем из оракула удаленную через интерфейс группу
    assert old_groups == new_groups  # Проверить, что удаленная группа отсутствует на странице, а остальные группы присутствуют

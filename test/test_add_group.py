# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(app):
    old_groups = app.group.get_group_list()  # Оракул. Получаем список групп со страницы, до выполнения действия
    group = Group("groupname", "groupheader", "groupfooter")
    app.group.create(group)  # Выполняем действие создания группы
    assert len(old_groups) + 1 == app.group.count()  # Проверяем, что после выполнения действия кол-во групп на странице увеличилось на 1
    new_groups = app.group.get_group_list()  # Получаем список групп со страницы, после выполнения действия
    old_groups.append(group)  # Оракул. Добавляем в оракула созданную через интерфейс группу
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)  # Проверить, что добавлення группа присутствует на странице



def test_create_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group("", "", "")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



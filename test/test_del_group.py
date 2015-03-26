# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group for delete"))
    old_groups = app.group.get_group_list()
    app.group.delete()
    new_groups = app.group.get_group_list() # Проверить, что после удаления кол-во групп уменьшилось на 1
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups  # Проверить, что удаленная группа отсутствует на странице, а остальные группы присутствуют

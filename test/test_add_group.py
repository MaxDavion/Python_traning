# -*- coding: utf-8 -*-
from model.group import Group

def test_create_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group("groupname", "groupheader", "groupfooter"))
    new_groups = app.group.get_group_list() ## Проверить, что после создания кол-во групп увеличилось на 1
    assert len(old_groups) + 1 == len(new_groups)


def test_create_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group("", "", ""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)   ## Проверить, что после создания кол-во групп увеличилось на 1


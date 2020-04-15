# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new group"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    group = Group(name="edit name")
    group.element_id = old_groups[index].element_id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="new group"))
#     old_groups = app.group.get_groups_list()
#     app.group.edit_first_group(Group(header="edit header"))
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) == len(new_groups)

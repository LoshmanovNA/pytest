# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new group"))
    old_groups = app.group.get_groups_list()
    app.group.edit_first_group(Group(name="edit name"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new group"))
    old_groups = app.group.get_groups_list()
    app.group.edit_first_group(Group(header="edit header"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)

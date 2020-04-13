# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new group"))
    app.group.edit_first_group(Group(name="edit name"))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new group"))
    app.group.edit_first_group(Group(header="edit header"))

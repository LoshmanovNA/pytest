# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_groups_list()) == 0:
        app.group.create(Group(name="new group"))
    old_groups = db.get_groups_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.element_id)
    new_groups = db.get_groups_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        def clean(gr):
            return Group(element_id=gr.element_id, name=gr.name.strip())
        new_groups = map(clean, new_groups)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)

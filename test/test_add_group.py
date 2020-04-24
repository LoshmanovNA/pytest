# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_groups_list()
    app.group.create(group)
    new_groups = db.get_groups_list()
    old_groups.append(group)
    assert old_groups == new_groups
    if check_ui:
        def clean(gr):
            return Group(element_id=gr.element_id, name=gr.name.strip())

        new_groups = map(clean, new_groups)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)

# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_group(app, db, data_groups, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="new group"))
    old_groups = db.get_groups_list()  # Получаем список групп из БД
    group_data = data_groups  # Создаем данные, которыми заменим существующие значения у группы
    group = random.choice(old_groups)  # Выбираем случайную группу для редактирования
    index = old_groups.index(group)  # Сохраянем индекс группы для последующего обращения к ней
    app.group.edit_group_by_id(group.element_id, group_data)  # Редактируем имя группы
    new_groups = db.get_groups_list()  # Получаем новый список групп, среди которых отредактированнная
    old_groups[index].__dict__['name'] = group_data.__dict__['name']  # Находим в старом списке отредактированную в UI
    # группу и правим ей имя, для получения эталона ожидаемого результата
    assert old_groups == new_groups  # Сравниваем ожидаемый результат со значением в БД
    if check_ui:
        def clean(gr):
            return Group(element_id=gr.element_id, name=gr.name.strip())

        new_groups = map(clean, new_groups)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)

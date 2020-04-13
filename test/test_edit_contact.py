# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_fio(app):
    app.contact.edit_first_contact(Contact(first_name='Тест 1',
                                           middle_name='Тестович 1',
                                           last_name='Тестов 1'))

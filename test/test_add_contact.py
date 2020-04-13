# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_empty_contact(app):
    app.contact.create(Contact(first_name='', middle_name='', last_name='',
                               nickname='', title='', company='', address='',
                               home_phone='', mobile_phone='', work_phone='', fax='',
                               email_1='', email_2='', email_3='', homepage='',
                               day_of_birth='-', month_of_birth='-', year_of_birth='-',
                               anniversary_day='-', anniversary_month='-', anniversary_year='-',
                               address_2='', phone_2='', notes=''))


def test_add_contact(app):
    app.contact.create(Contact(first_name='Тест', middle_name='Тестович', last_name='Тестов',
                               nickname='QA', title='Тестировщик', company='СофтКо', address='Москва',
                               home_phone='911', mobile_phone='8800', work_phone='144', fax='310000',
                               email_1='test_1@test.ru', email_2='test_2@test.ru', email_3='test_3@test.ru', homepage='www.test.ru',
                               day_of_birth='1', month_of_birth='January', year_of_birth='1991',
                               anniversary_day='31', anniversary_month='April', anniversary_year='2020',
                               address_2='Лос-Анжелес', phone_2='+3310333', notes='Заметка'))


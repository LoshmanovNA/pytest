# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name='Тест 1', middle_name='Тестович 1', last_name='Тестов 1',
                               nickname='QA 1', title='Тестировщик 1', company='СофтКо 1', address='Москва',
                               home_phone='911', mobile_phone='8800', work_phone='144', fax='310000',
                               email_1='test_1@test.ru', email_2='test_2@test.ru', email_3='test_3@test.ru', homepage='www.test.ru',
                               day_of_birth='1', month_of_birth='January', year_of_birth='1991',
                               anniversary_day='31', anniversary_month='April', anniversary_year='2020',
                               address_2='Лос-Анжелес', phone_2='+3310333', notes='Заметка'))
    app.session.logout()

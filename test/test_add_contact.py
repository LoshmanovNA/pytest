# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


@pytest.mark.contact
def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name='Тест', middle_name='Тестович', last_name='Тестов',
                      mobile_phone='8800', home_phone='310337', work_phone='1234321',
                      phone_2='7950132')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



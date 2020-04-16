# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import pytest


@pytest.mark.contact
def test_edit_contacts_first_name_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Test", middle_name="Testovich", last_name="Testov"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name='Редактий')
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index].first_name = contact.first_name
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


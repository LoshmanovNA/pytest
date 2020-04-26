# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import pytest


@pytest.mark.contact
def test_edit_contacts_first_name_by_index(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Test", middle_name="Testovich", last_name="Testov"))
    old_contacts = db.get_contacts_list()
    contact_data = Contact(first_name='Редактий')
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    app.contact.edit_contact_by_id(contact.id, contact_data)
    new_contacts = db.get_contacts_list()
    old_contacts[index].__dict__['first_name'] = contact_data.__dict__['first_name']
    assert old_contacts == new_contacts
    if check_ui:
        def clean(cont):
            return Contact(id=cont.id, first_name=cont.first_name.strip(), last_name=cont.last_name.strip())

        new_contacts = map(clean, new_contacts)
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(),
                                                                     key=Contact.id_or_max)


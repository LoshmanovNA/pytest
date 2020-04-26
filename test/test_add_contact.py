# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


@pytest.mark.contact
def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contacts_list()
    app.contact.create(contact)
    new_contacts = db.get_contacts_list()
    old_contacts.append(contact)
    assert old_contacts == new_contacts
    if check_ui:
        def clean(cont):
            return Contact(id=cont.id, first_name=cont.first_name.strip(), last_name=cont.last_name.strip())

        new_contacts = map(clean, new_contacts)
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)



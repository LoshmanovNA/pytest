from model.contact import Contact
from random import randrange
import pytest


@pytest.mark.contact
def test_delete_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Test", middle_name="Testovich", last_name="Testov"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

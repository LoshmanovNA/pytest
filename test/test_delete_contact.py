from model.contact import Contact
import random
import pytest
import time

@pytest.mark.contact
def test_delete_contact_by_id(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Test", middle_name="Testovich", last_name="Testov"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    print('Выбранный контакт', contact)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(2)
    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact)
    print('Старые контакты', old_contacts)
    print('Новые контакты', new_contacts)
    assert old_contacts == new_contacts
    if check_ui:
        def clean(cont):
            return Contact(id=cont.id, first_name=cont.first_name.strip(), last_name=cont.last_name.strip())

        new_contacts = map(clean, new_contacts)
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)

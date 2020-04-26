from model.contact import Contact


def test_address_on_home_page(app, orm):
    contacts_from_home_page = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(orm.get_contact_list(), key=Contact.id_or_max)

    for i in range(len(contacts_from_db)):
        assert contacts_from_db[i].address.strip() == contacts_from_home_page[i].address.strip()

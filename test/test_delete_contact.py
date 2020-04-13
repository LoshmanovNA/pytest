from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Test", middle_name="Testovich", last_name="Testov"))
    app.contact.delete_first_contact()

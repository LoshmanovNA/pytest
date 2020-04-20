# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(maxlen, is_only_digits=False):
    digits = string.digits + " ()-"
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    result_string = "".join([random.choice(digits) for i in range(random.randrange(maxlen))]) \
        if is_only_digits \
        else "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return result_string


test_data = [
    Contact(first_name=first_name, last_name=last_name, mobile_phone=mobile,
            home_phone=home, work_phone=work, phone_2=phone_2)
    for first_name in ["", random_string(10)]
    for last_name in ["", random_string(10)]
    for mobile in ["", random_string(7, is_only_digits=True)]
    for home in ["", random_string(7, is_only_digits=True)]
    for work in ["", random_string(7, is_only_digits=True)]
    for phone_2 in ["", random_string(7, is_only_digits=True)]
]


@pytest.mark.parametrize('contact', test_data, ids=[repr(x) for x in test_data])
@pytest.mark.contact
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



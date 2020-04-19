

def test_emails_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def merge_emails_like_on_home_page(contact):
    return "\n".join([contact.email_1, contact.email_2, contact.email_3])

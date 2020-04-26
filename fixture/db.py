import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host,
        self.name = name,
        self.user = user,
        self.password = password
        self.connection = pymysql.connect(host=host,
                                          database=name,
                                          user=user,
                                          password=password,
                                          autocommit=True)

    def get_groups_list(self):
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                lst.append(Group(element_id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return lst

    def get_contacts_list(self):
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home, mobile, work, phone2 "
                           "from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, first_name, last_name, home, mobile, work, phone2) = row
                lst.append(Contact(id=str(id), first_name=first_name, last_name=last_name, home_phone=home,
                                   mobile_phone=mobile, work_phone=work, phone_2=phone2))
        finally:
            cursor.close()
        return lst

    def destroy(self):
        self.connection.close()

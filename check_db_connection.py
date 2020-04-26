import pymysql.cursors
from fixture.orm import ORMFixture

db = ORMFixture(host='192.168.64.2',
                name='addressbook',
                user='admin',
                password='admin')

try:
    l = db.get_contact_list()
    for i in range(len(l)):
        print(l[i].address)
    print(len(l))
finally:
    pass # db.destroy()

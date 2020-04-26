import pymysql.cursors

connection = pymysql.connect(host='192.168.64.2',
                             database='addressbook',
                             user='admin',
                             password='admin')

try:
    cursor = connection.cursor()
    cursor.execute("select firstname, lastname, home, mobile, work, phone2 "
                   "from addressbook where deprecated='0000-00-00 00:00:00'")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()

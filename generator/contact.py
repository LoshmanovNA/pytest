from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(maxlen, is_only_digits=False):
    digits = string.digits + " ()-"
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    result_string = "".join([random.choice(digits) for i in range(random.randrange(maxlen))]) \
        if is_only_digits \
        else "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return result_string


test_data = [Contact(first_name="", last_name="", mobile_phone="",
                     home_phone="", work_phone="", phone_2="")] + [
    Contact(first_name=random_string(10), last_name=random_string(10),
            mobile_phone=random_string(7, is_only_digits=True),
            home_phone=random_string(7, is_only_digits=True),
            work_phone=random_string(7, is_only_digits=True),
            phone_2=random_string(7, is_only_digits=True))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))

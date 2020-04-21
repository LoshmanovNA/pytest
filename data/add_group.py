from model.group import Group
import random
import string

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string(10)]
    for header in ["", random_string(20)]
    for footer in ["", random_string(20)]
]

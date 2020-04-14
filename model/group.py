

class Group:

    def __init__(self, name=None, header=None, footer=None, element_id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.element_id = element_id

    def __repr__(self):
        return f"{self.element_id} : {self.name}"

    def __eq__(self, other):
        return self.element_id == other.element_id and self.name == other.name

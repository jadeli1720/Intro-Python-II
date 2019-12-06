# Implement a class to hold item information

class Item: #base class
    """
    This is a item class with attributes
    name & description
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
    

    def __repr__(self):
        return f"{self.name}, {self.description}"

    
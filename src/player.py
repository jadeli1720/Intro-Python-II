# Write a class to hold player information, e.g. what room they are in
# currently. --> four lines: name, current location,

from item import Item

class Player:
    """
    This is a player call with the attributes:
    name, current_room....
    """
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        # self.inventory = []

    def __repr__(self):
        return (f'{self.current_room.name}')  
    def __str__(self):
        return (f"{self.name}")

    def move(self, direction):
        str = f'{direction}_to'
        new_room = getattr(self.current_room, str)

        if new_room:
            self.current_room = new_room

    def add_item(self, item):
        self.items.append(item)
        test = Item(item, "thing")
        test.on_take()
        

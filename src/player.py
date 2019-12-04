# Write a class to hold player information, e.g. what room they are in
# currently. --> four lines: name, current room,

class Player:
    """
    This is a player call with the attributes:
    name, current_room....
    """
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

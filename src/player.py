# Write a class to hold player information, e.g. what room they are in
# currently. --> four lines: name, current location,

class Player:
    """
    This is a player call with the attributes:
    name, current_room....
    """
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __repr__(self):
        return (f'{self.current_room.name}')  
    def __str__(self):
        return (f"{self.name}")

# Implement a class to hold room information. 
# Attributes: name, description


class Room:
    """
    This is a room class with the attributes:
    room, description, and the 4 cardinal directions set to None
    """
    def __init__(self, room, description):
        self.room = room
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
    
    def __repr__(self):
        return f"{self.room}"


    # directions --> n_to, s_to, e_to, w_to --> attribute 

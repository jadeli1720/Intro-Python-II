# Implement a class to hold room information. 
# Attributes: name, description


class Room:
    """
    This is a room class with the attributes:
    room, description, and the 4 cardinal directions set to None
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return f"{self.name}"

   
    
    

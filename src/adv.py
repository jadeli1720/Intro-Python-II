from room import Room
from player import Player
# from textwrap import wrap
import textwrap

# Declare all the rooms(5)-->Room class: room title, room description
# Room Dictionary
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together (connect) --> direction attributes --> define n_to = none which equals to null for movement; will switch when a player moves into the room

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

def adventrue_game():
        print("Welcome! Move along the 4 cardinal points. Type in n, s, e, or w. To quit type q")

if __name__ == '__main__':
  adventrue_game()

# Make a new player object that is currently in the 'outside' room.
player = Player("Player 1", room['outside'])

text_wrapper = textwrap.TextWrapper()

choices = ['n', 's', 'e', 'w']

# Global function to help actually move a player
def move(n_to):
    player.room = player.room.n_to
    # player.room = player.room.s_to
    # player.room = player.room.w_to
    # player.room = player.room.e_to
    

# Write a loop that: --> Create a REPL loop to process 'n', commands
while True:

    # * Prints the current room name
    print(f"{player.name}, you are currently at the {player.room}")

    # * Prints the current description (the textwrap module might be useful here).
    print(text_wrapper.wrap(f"{player.room.description}"))

    # * Waits for user input and decides what to do.

    # choice = input("Move('n', 's', 'e', 'w')")    
    choice = input("->")  

    # If the user enters a cardinal direction, attempt to move to the room there.
    # If player chooses 'n' & players location is room['outside'] move here
    # directions --> n_to, s_to, e_to, w_to ==> ATTRIBUTES...must check
    if choice == 'n' and hasattr(player.room, 'n_to'):
        print(f"Your have moved North")
        # player.room = player.room.n_to
        move('n_to')
        # print(player.room)
        
        
    elif choice == 's' and hasattr(player.room, 's_to'):
        print(f"Your have moved South to the")
        # need figure how to move the player

    elif choice == 'e':
        print(f"Your have moved East to the")
        # need figure how to move the player

    elif choice == 'w':
        print(f"Your have moved West to the")
        # need figure how to move the player

    # Print an error message if the movement isn't allowed.

    # If the user enters "q", quit the game.
    elif choice == "q":
        print ("Thank you for playing. Goodbye!")
        break
   



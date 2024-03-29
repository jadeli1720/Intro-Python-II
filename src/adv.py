from room import Room 
from player import Player
from item import Item
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

# Item 
maps = Item("map", "Old and faded")
rag = Item("rag", "Dirty old")
flashlight = Item("flashlight", "Cracked")
compass = Item("compass", "Rusty")

gold = Item("golden statue", "Beautiful, dazzling")

# Appending items to the rooms
room['outside'].items.append(maps)
room['narrow'].items.append(rag)
room['foyer'].items.append(flashlight)
room['overlook'].items.append(compass)
room['treasure'].items.append(gold)


#
# Main
#

def divider():
    print(f"========================================\n")

def adventrue_game():
        print("Welcome to 'The Adventure Game'!")

if __name__ == '__main__':
    adventrue_game()


def current_room():
    print(text_wrapper.wrap(f"{player.current_room.description}"))
    divider()

def items():
    print(f'Item: {player.current_room.items}')

divider()

# Make a new player object that is currently in the 'outside' room.
name = input("Please enter your name:" )
divider()
player = Player(name, room['outside'])

text_wrapper = textwrap.TextWrapper()



# * Prints the current room name

print(f"{player.name}, you are currently at the {player.current_room}")

# Prints Item in the room
print(f'Item: {player.current_room.items}')
# * Prints the current description (the textwrap module might be useful here).
current_room()

print(f"Please choose a direction by typing: n, s, e, or w\n", )

    

# Write a loop that: --> Create a REPL loop to process 'n', commands
while True:

    # * Waits for user input and decides what to do.
    choice = input("->")  

    # If the user enters a cardinal direction, attempt to move to the room there.
    # If player chooses 'n' & players location is room['outside'] move here
    # directions --> n_to, s_to, e_to, w_to ==> ATTRIBUTES...must check for
    if choice == 'n' and hasattr(player.current_room, 'n_to'):
        player.move('n')
        print(f"Your have moved North to the {player.current_room}")
        current_room()
        print(f'Item: {player.current_room.items}')

    elif choice == 's' and hasattr(player.current_room, 's_to'):
        player.move('s')
        print(f"Your have moved South to the {player.current_room}")
        current_room()

    elif choice == 'e' and hasattr(player.current_room, 'e_to'):
        player.move('e')
        print(f"Your have moved East to the {player.current_room}")
        current_room()

    elif choice == 'w' and hasattr(player.current_room, 'w_to'):
        player.move('w')
        print(f"Your have moved West to the {player.current_room}")
        current_room()

    # If the user enters "q", quit the game.
    elif choice == "q":
        print ("\nThank you for playing. Goodbye!")
        break

    # Print an error message if the movement isn't allowed.
    else:
        print(f"\nSorry, you can't go that way. Please try again!\n")
   



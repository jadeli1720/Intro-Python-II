from room import Room
from player import Player
# from textwrap import wrap
import textwrap

# Declare all the rooms(5)-->Room class: room title, room description

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

# Make a new player object that is currently in the 'outside' room.
player1 = Player("Player 1", room['outside'])

text_wrapper = textwrap.TextWrapper()

choices = ['n', 's', 'e', 'w']

print(f"{player1.name}, you are currently at the {player1.current_location}")

print(text_wrapper.wrap(f"{player1.current_location.description}"))


# Write a loop that: --> Create a REPL loop to process commands
# while True:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
#     #direction = input("choose what room you want move to by typing in one of the for cardinal directions: n, s, e, w ")
#     def current_room():
#         print("Choose which way you want to move! n, s, e, w")
# If the user enters a cardinal direction, attempt to move to the room there.

# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.


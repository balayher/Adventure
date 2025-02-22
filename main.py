from constants import *
from dungeon import create_dungeon, create_objects
from player import Player
import random

def main():
    # setting up the dungeon, in-game objects, and player
    # generates a random code for the safe puzzle
    dungeon = create_dungeon()
    objects = create_objects()
    player = Player(
        STARTING_X_POS, 
        STARTING_Y_POS,
        STARTING_DIRECTION, 
        STARTING_INVENTORY,
        PROG,
        random.randint(1000, 9999)
        )

    # introduction to the game
    print(
        "You awaken in an unfamiliar place.\n" 
        "The last thing you remember is breaking into Dr. Evan's mansion in search of his most prized possession.\n"
        "It seems you were unsucessful as you are now inside a prison cell.\n"
        "How are you going to get out of this one?"
    )

    # gameplay loop
    while True:
        # get action command from player (.lower() used to ignore case)
        action = input("What would you like to do? ").lower()
        player.check_action(dungeon, action, objects)

        # check if game should be closed
        if player.prog == 100:
            print("Exiting game.")
            return
        

main()
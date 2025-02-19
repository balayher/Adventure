from constants import *
from dungeon import create_dungeon
from player import Player

def main():
    # setting up the dungeon and player
    dungeon = create_dungeon()
    player = Player(
        STARTING_X_POS, 
        STARTING_Y_POS, 
        dungeon[STARTING_X_POS][STARTING_Y_POS].name, 
        STARTING_DIRECTION, 
        STARTING_INVENTORY,
        PROG
        )

    # introduction to the game
    print(
        "You approach a murky house in the forest. You feel shivers down your spine."
        "The treasures you seek must be inside! You quickly enter and shut the door behind you."
        )
    player.enter_room(dungeon)

    # gameplay loop
    while True:
        # get action command from player (.lower() used to ignore case)
        action = input("What would you like to do? ")
        action = action.lower()
        player.check_action(dungeon, action)

        # check if game should be closed
        if player.prog == 100:
            print("Exiting game.")
            return
        

main()
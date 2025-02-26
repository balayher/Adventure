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
        "It seems you were unsuccessful as you are now inside a prison cell.\n"
        "How are you going to get out of this one?"
    )
    
    dungeon[STARTING_X_POS][STARTING_Y_POS].visited = True

    # gameplay loop
    while True:
        # get action command from player (.lower() used to ignore case)
        action = input("\nWhat would you like to do? ").lower()
        player.check_action(dungeon, action, objects)

        # check if player exit's the mansion
        if player.prog == 77:
            print("CONGRATULATIONS! YOU'VE WON!\n")
            input("Press Enter for the epilogue...")
            # checks if you took the chef's fish
            if "Fish" not in dungeon[0][0].items:
                print("\nChef Rainslayer was dismayed that her fish went missing.")
            else:
                print("\nChef Rainslayer's magical soup paired greatly with the red herring.")

            print("Kujo quit his job as Evan's Guard.")
            # checks how you got past the guard
            if objects["Guard"].prog == 3:
                print("He found a less dangerous position filing TPS reports.")
            if objects["Guard"].prog == 4:
                print("He sold Evan's treasure and moved to the Bahamas.")

            print("Evan was not pleased to learn that you escaped.")
            if "Brain" in player.inv or objects["Guard"].prog == 4:
                print(
                    "Once he found out his treasure was missing, he immediately went berserk.\n"
                    "Evan took his lion Roary and gathered his friends to hunt you down..."
                )
            else:
                print("He felt relieved that his prized golden brain was safe.")
                if objects["Vase"].prog == 1 or objects["Rug"].prog == 2:
                    print("Although he was quite annoyed about the other damages around the property...")
                    if objects["Sink"].prog == 1 or objects["Shower"].prog == 1:
                        print("He also pondered why the water was left running...")
                else:
                    if objects["Sink"].prog == 1 or objects["Shower"].prog == 1:
                        print("Though he pondered why the water was left running...")

            input("\nPress Enter to continue...")

            if "Brain" in player.inv and "Coin" in player.inv:
                print(
                    "\nYou escaped with Evan's prized treasure and the gold coin.\n"
                    "Well done!"
                )
            elif "Brain" in player.inv:
                print(
                    "\nYou escaped with Evan's prized treasure.\n"
                    "You wonder if you could have gotten some coinage as well..."
                )
            elif "Coin" in player.inv:
                print(
                    "\nYou failed to escape with Evan's treasure, but you did get a gold coin.\n"
                    "Was there a way to have both?"
                )
            else:
                print(
                    "\nYou failed to escape with anything of value.\n"
                    "What treasures did you miss out on?"
                )
            print("\nExiting game.")
            return

        # check if game should be closed
        if player.prog == 100:
            print("Exiting game.")
            return
        
main()
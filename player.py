from constants import *
from inspect import inspect_room
from items import check_item, take_item, use_item
from room_desc import get_room_desc

class Player():
    def __init__(self, x, y, direction, inv, prog, code):
        # x and y represent the player's current position
        # room is the name of the room the player is currently in
        # direction is the current direction the player is facing
        # inv is the player's current inventory of items
        # prog is the player's current progression level
        # code is the safe code
        
        self.cur_pos_x = x
        self.cur_pos_y = y
        self.direction = direction
        self.inv = inv
        self.prog = prog
        self.code = code
        
    def enter_room(self, dungeon):
        # move player into another room, printing the room's name and description
        x = self.cur_pos_x
        y = self.cur_pos_y
        print(f"You have entered the {dungeon[x][y].name}.")
        get_room_desc(dungeon[x][y])

    def check_action(self, dungeon, action, objects):
        #initializing variables for ease of use later
        x = self.cur_pos_x
        y = self.cur_pos_y

        # checks if the player submitted a valid action
        match action:
            # move to another room
            case "move" | "m":
                self.move_action(dungeon)

            # exit the game
            case "exit" | "e":
                confirm = input("Are you sure you want to exit the game? ").lower()
                if confirm == "yes" or confirm == "y":
                    self.prog = 100

            # look around the current room
            case "look" | "l":
                print()
                inspect_room(dungeon[x][y])

            # check an item your inventory or the current room
            case "check" | "c":
                item = input("What would you like to check? ").capitalize()
                print()
                check_item(self, dungeon[x][y], item, objects)

            # attempt to take an item from the current room
            case "grab" | "g" | "take" | "t":
                item = input("What would you like to grab? ").capitalize()
                print()
                take, item = take_item(self, dungeon[x][y], item, objects)
                if take == True:
                    self.inv.add(item)
                    dungeon[x][y].items.remove(item)
                    print(f"You add the {item} to your inventory.")  

            # check your current inventory 
            case "inventory" | "inv" | "i" | "bag" | "b" :
                print()
                if len(self.inv) == 0:
                    print("You currently have nothing.")
                else:
                    print("You have the following items:")
                    for item in self.inv:
                        print(item)

            # use an item from your inventory
            case "use" | "u":
                item = input("What item would you like to use? ").capitalize()
                print()
                remove = use_item(self, dungeon[x][y], item, objects)
                if remove == True:
                    self.inv.remove(item)

            # easter egg actions
            case "dance":
                print("You get a sudden urge to dance, but think better of it.")
            
            case "debut":
                dungeon[x][y].exits = [True, True, True, True]

            case "safe":
                print(f"The safe code is {self.code}. Delete this after testing.")
                print(self.code // 1000)
                print((self.code % 1000) // 100)
                print((self.code % 100) // 10)
                print(self.code % 10)

            # not a valid action
            case _:
                print("Invalid action.")

    def move_action(self, dungeon):
        # initializing variables for ease of use, move = 4 for movement failure
        x = self.cur_pos_x
        y = self.cur_pos_y
        facing = self.direction
        direction = input("Which direction would you like to move? ").lower()
        print()

        # North = 0, East = 1, South = 2, West = 3
        # cardinal direction movement
        match direction:
            case "north" | "n" | "up" | "u":
                move = 0
            case "east" | "e":
                move = 1
            case "south" | "s" | "down" | "d":
                move = 2
            case "west" | "w":
                move = 3
            case "forwards" | "forward" | "f":
                move = facing
            case "right" | "r":
                move = (facing + 1) % 4
            case "backwards" | "backward" | "b" | "back":
                move = (facing + 2) % 4
            case "left" | "l":
                move = (facing + 3) % 4
            case _:
                print("Invalid direction.")
                return
        
        # check if movement in the given direction is possible
        if dungeon[x][y].exits[move] == False:
            print("You cannot proceed in that direction.")
            return

        # updates the player's facing
        self.direction = move
    
        # move to the adjacent room
        # North = 0, East = 1, South = 2, West = 3
        match move:
            case 0:
                self.cur_pos_y -= 1
            case 1:
                self.cur_pos_x += 1
            case 2:
                self.cur_pos_y += 1
            case 3:
                self.cur_pos_x -= 1
            case _:
                print("How did this happen?")

        self.enter_room(dungeon)
    
from constants import *

class Player():
    def __init__(self, x, y, room, direction, inv, prog):
        # x and y represent the player's current position
        # room is the name of the room the player is currently in
        # direction is the current direction the player is facing
        # inv is the player's current inventory of items
        # prog is the player's current progression level
        
        self.cur_pos_x = x
        self.cur_pos_y = y
        self.cur_room = room
        self.direction = direction
        self.inv = inv
        self.prog = prog
        
    def enter_room(self, dungeon):
        # move player into another room, printing the room's name and description
        x = self.cur_pos_x
        y = self.cur_pos_y
        self.room = dungeon[x][y].name
        print(f"You have entered the {dungeon[x][y].name}.")
        print(dungeon[x][y].desc)

    def check_action(self, dungeon, action):
        # checks if the player submitted a valid action
        match action:
            case "move" | "m":
                self.move_action(dungeon)
            case "exit" | "e":
                confirm = input("Are you sure you want to exit the game? ")
                confirm = confirm.lower()
                if confirm == "yes" or confirm == "y":
                    self.prog = 100
            case _:
                print("Invalid action.")

    def move_action(self, dungeon):
        # initializing variables for ease of use, move = 4 for movement failure
        x = self.cur_pos_x
        y = self.cur_pos_y
        facing = self.direction
        direction = input("Which direction would you like to move? ").lower()
        
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
    
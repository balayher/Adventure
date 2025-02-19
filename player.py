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
        x = self.cur_pos_x
        y = self.cur_pos_y
        self.room = dungeon[x][y].name
        print(f"You have entered the {dungeon[x][y].name}.")
        print(dungeon[x][y].desc)

    def check_action(self, dungeon, action):
        if action == "move" or action == "m":
            self.move_action(dungeon)
            return
        if action == "exit":
            confirm = input("Are you sure? ")
            confirm = confirm.lower()
            if confirm == "yes" or confirm == "y":
                self.prog = 100
                return
            return
        print("Invalid action.")
        return

    def move_action(self, dungeon):
        x = self.cur_pos_x
        y = self.cur_pos_y
        facing = self.direction
        move = 4
        direction = input("Which direction would you like to move? ")
        direction = direction.lower()
        if direction == "north" or direction == "n" or direction == "up" or direction == "u":
            move = 0
        if direction == "east" or direction == "e":
            move = 1
        if direction == "south" or direction == "s" or direction == "down" or direction == "d":
            move = 2
        if direction == "west" or direction == "w":
            move = 3
        if direction == "forwards" or direction == "forward" or direction == "f":
            move = facing
        if direction == "right" or direction == "r":
            move = (facing + 1) % 4
        if direction == "backwards" or direction == "backward" or direction == "b":
            move = (facing + 2) % 4
        if direction == "left" or direction == "l":
            move = (facing + 3) % 4
    
        if move == 4:
            print("Invalid direction.")
            return

        if dungeon[x][y].exits[move] == False:
            print("You cannot proceed in that direction.")
            return
    
        if move == 0:
            self.cur_pos_y -= 1
            self.enter_room(dungeon)
            return
        if move == 1:
            self.cur_pos_x += 1
            self.enter_room(dungeon)
            return
        if move == 2:
            self.cur_pos_y += 1
            self.enter_room(dungeon)
            return
        if move == 3:
            self.cur_pos_x -= 1
            self.enter_room(dungeon)
            return
    
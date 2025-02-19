from constants import *

class Player():
    def __init__(self, x, y, room, direction, inv):
        # x and y represent the player's current position
        # room is the name of the room the player is currently in
        # direction is the current direction the player is facing
        # inv is the player's current inventory of items
        
        self.cur_pos_x = x
        self.cur_pos_y = y
        self.cur_room = room
        self.direction = direction
        self.inv = inv
        


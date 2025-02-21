

class Room():
    def __init__(self, x, y, exits, name, items, prog):
        # x_pos and y_pos are the room's position in the dungeon
        # exits are the directions that the player can currently leave the room
        # exits is a True/False list of [North, East, South, West]
        # name is the room's name
        # items are the objects currently in the room
        # prog is the room's progression value
        # prog is used to determine the state of the room and which descriptions to print
        
        self.x_pos = x
        self.y_pos = y
        self.exits = exits
        self.name = name
        self.items = items
        self.prog = prog
        
        
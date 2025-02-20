

class Room():
    def __init__(self, x, y, exits, name, items, prog):
        self.x_pos = x
        self.y_pos = y
        self.exits = exits
        self.name = name
        self.items = items
        self.prog = prog
        
        
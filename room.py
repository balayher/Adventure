

class Room():
    def __init__(self, x, y, exits, name, desc, items, progress):
        self.x_pos = x
        self.y_pos = y
        self.exits = exits
        self.name = name
        self.desc = desc
        self.items = items
        self.progress = progress
        
        
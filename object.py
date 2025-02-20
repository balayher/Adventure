

class Object():
    def __init__(self, name, collect=False, inv=False, prog=0):
        # name is the name of the object
        # collect indicates if the object is collectable
        # inv indicates if the player has the object in their inventory
        # prog is the object's current progression level
        
        self.name = name
        self.collect = collect
        self.inv = inv
        self.prog = prog
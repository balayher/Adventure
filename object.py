

class Object():
    def __init__(self, collect=False, prog=0):
        # name is the name of the object
        # collect indicates if the object is collectable
        # inv indicates if the player has the object in their inventory
        # prog is the object's current progression level
        
        self.collect = collect
        self.prog = prog
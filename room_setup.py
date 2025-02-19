# A list of all the room names in the dungeon

R0_0 = "Armory"
R0_1 = "Hallway"
R1_0 = "Kitchen"
R1_1 = "Foyer"

ROOMS = [[R0_0, R0_1],[R1_0, R1_1]]

# A list of the interactable objects in a room

I0_0 = ["Sword", "Shield"]
I0_1 = ["Door"]
I1_0 = ["Chef", "Knife", "Fish"]
I1_1 = ["Rug"]

ITEMS = [[I0_0, I0_1],[I1_0, I1_1]]

# A list of which directions the player can exit a room at the start of the game
# Format is [North, East, South, West]

E0_0 = [False, True, False, False]
E0_1 = [False, False, True, False]
E1_0 = [False, True, False, False]
E1_1 = [True, True, False, False]

EXITS = [[E0_0, E0_1],[E1_0, E1_1]]

# A Progress value that tracks advancement through the room

PROG = 0
# A list of all the room names in the dungeon

R0_0 = "Armory"
R0_1 = "Kitchen"
R1_0 = "Hallway"
R1_1 = "Foyer"

ROOMS = [[R0_0, R0_1],[R1_0, R1_1]]

# Sets of the interactable objects in a room

I0_0 = {"Sword", "Shield"}
I0_1 = {"Chef", "Knife", "Fish"}
I1_0 = {"Door"}
I1_1 = {"Rug"}

ITEMS = [[I0_0, I0_1],[I1_0, I1_1]]

# A list of which directions the player can exit a room at the start of the game
# Format is [North, East, South, West]

E0_0 = [False, True, False, False]
E0_1 = [False, True, False, False]
E1_0 = [False, False, True, False]
E1_1 = [True, False, False, True]

EXITS = [[E0_0, E0_1],[E1_0, E1_1]]

# A list of all the room names in the dungeon

R0_0 = "Kitchen"
R0_1 = "Dining Room"
R0_2 = "Closet"
R0_3 = "Treasury"
R1_0 = "Dungeon"
R1_1 = "Hallway"
R1_2 = "Corridor"
R1_3 = "Lounge"
R2_0 = "Bathroom"
R2_1 = "Passageway"
R2_2 = "Gallery"
R2_3 = "Foyer"
R3_0 = "Study"
R3_1 = "Living Room"
R3_2 = "Armory"
R3_3 = "Exit"

ROOMS = [
    [R0_0, R0_1, R0_2, R0_3],
    [R1_0, R1_1, R1_2, R1_3],
    [R2_0, R2_1, R2_2, R2_3],
    [R3_0, R3_1, R3_2, R3_3],
    ]

# Sets of the interactable objects in a room

I0_0 = {"Chef", "Knife", "Fish"}
I0_1 = {"Table", "Vase"}
I0_2 = {"Bucket", "Cans"}
I0_3 = {"Safe", "Keyring"}
I1_0 = {"Celldoor"}
I1_1 = {"Rug"}
I1_2 = {"Clock"}
I1_3 = {"Chair", "Sofa", "Diary"}
I2_0 = {"Sink", "Toilet", "Shower"}
I2_1 = {"Door"}
I2_2 = {"Statue", "Painting", "Metaldoor"}
I2_3 = {"Guard", "Stick"}
I3_0 = {"Candle", "Books"}
I3_1 = {"Tv", "Remote", "Fireplace"}
I3_2 = {"Sword", "Shield", "Armor"}
I3_3 = set()

ITEMS = [
    [I0_0, I0_1, I0_2, I0_3],
    [I1_0, I1_1, I1_2, I1_3],
    [I2_0, I2_1, I2_2, I2_3],
    [I3_0, I3_1, I3_2, I3_3],
    ]

# A list of which directions the player can exit a room at the start of the game
# Format is [North, East, South, West]

E0_0 = [False, False, True, False]
E0_1 = [True, True, True, False]
E0_2 = [True, False, False, False]
E0_3 = [False, True, False, False]
E1_0 = [False, False, True, False]
E1_1 = [True, True, False, True]
E1_2 = [False, True, True, False]
E1_3 = [True, True, False, True]
E2_0 = [False, False, True, False]
E2_1 = [True, True, True, True]
E2_2 = [True, True, False, True]
E2_3 = [False, True, False, True]
E3_0 = [False, False, True, False]
E3_1 = [True, False, False, True]
E3_2 = [False, False, False, True]
E3_3 = [False, False, False, True]

EXITS = [
    [E0_0, E0_1, E0_2, E0_3],
    [E1_0, E1_1, E1_2, E1_3],
    [E2_0, E2_1, E2_2, E2_3],
    [E3_0, E3_1, E3_2, E3_3],
    ]

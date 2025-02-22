from room import Room
from constants import *
from room_setup import ROOMS, ITEMS, EXITS
from object import Object

def create_dungeon():
    # creates a dungeon matrix of rooms for the player to travel between
    dungeon = []
    for i in range(DUNGEON_COLS):
        column = []
        for j in range(DUNGEON_ROWS):
            room = Room(i, j, EXITS[i][j], ROOMS[i][j], ITEMS[i][j], PROG)
            column.append(room)
        dungeon.append(column)
    return dungeon

def create_objects():
    # creates all the interactable items in the dungeon
    return {
        "Handkerchief": Object(True),
        "Chef": Object(),
        "Knife": Object(),
        "Fish": Object(True),
        "Table": Object(),
        "Vase": Object(),
        "Bucket": Object(True),
        "Cans": Object(),
        "Rice": Object(),
        "Safe": Object(),
        "Keyring": Object(),
        "Brain": Object(True),
        "Celldoor": Object(),
        "Rug": Object(),
        "Coin": Object(True),
        "Clock": Object(),
        "Chair": Object(),
        "Sofa": Object(),
        "Diary": Object(True),
        "Sink": Object(),
        "Toilet": Object(),
        "Shower": Object(),
        "Soap": Object(True),
        "Door": Object(),
        "Statue": Object(),
        "Painting": Object(),
        "Metaldoor": Object(),
        "Guard": Object(),
        "Stick": Object(True),
        "Books": Object(),
        "Candle": Object(True),
        "Tv": Object(),
        "Remote": Object(),
        "Fireplace": Object(),
        "Key": Object(),
        "Sword": Object(True),
        "Shield": Object(),
        "Armor": Object(),
    }

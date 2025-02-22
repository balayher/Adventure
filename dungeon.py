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
        "Handkerchief": Object(),
        "Chef": Object(),
        "Knife": Object(),
        "Fish": Object(),
        "Table": Object(),
        "Vase": Object(),
        "Bucket": Object(),
        "Cans": Object(),
        "Rice": Object(),
        "Safe": Object(),
        "Keyring": Object(),
        "Brain": Object(),
        "Celldoor": Object(),
        "Rug": Object(),
        "Coin": Object(),
        "Clock": Object(),
        "Chair": Object(),
        "Sofa": Object(),
        "Diary": Object(),
        "Sink": Object(),
        "Toilet": Object(),
        "Shower": Object(),
        "Soap": Object(),
        "Door": Object(),
        "Statue": Object(),
        "Painting": Object(),
        "Metaldoor": Object(),
        "Guard": Object(),
        "Stick": Object(),
        "Books": Object(),
        "Candle": Object(),
        "Tv": Object(),
        "Remote": Object(),
        "Fireplace": Object(),
        "Key": Object(),
        "Sword": Object(),
        "Shield": Object(),
        "Armor": Object(),
    }

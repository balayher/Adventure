from room import Room
from constants import *
from room_setup import ROOMS, ITEMS, EXITS
from room_desc import DESC
from object import Object

def create_dungeon():
    # creates a dungeon matrix of rooms for the player to travel between
    dungeon = []
    for i in range(DUNGEON_COLS):
        column = []
        for j in range(DUNGEON_ROWS):
            room = Room(i, j, EXITS[i][j], ROOMS[i][j], DESC[i][j], ITEMS[i][j], PROG)
            column.append(room)
        dungeon.append(column)
    return dungeon

def create_objects():
    return {
        "Sword": Object("Sword", True),
        "Shield": Object("Shield"),
        "Chef": Object("Chef"),
        "Knife": Object("Knife"),
        "Fish": Object("Fish", True),
        "Door": Object("Door"),
        "Rug": Object("Rug"),
    }
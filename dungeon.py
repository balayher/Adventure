from room import Room
from constants import *
from room_setup import ROOMS, ITEMS
from room_desc import DESC

def create_dungeon():
    dungeon = []
    for i in range(DUNGEON_COLS):
        column = []
        for j in range(DUNGEON_ROWS):
            room = Room(i, j, EXITS[i][j], ROOMS[i][j], DESC[i][j], ITEMS[i][j], PROG)
            column.append(room)
        dungeon.append(column)
    return dungeon


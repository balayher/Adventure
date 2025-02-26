from constants import *

def view_map(dungeon):
    print("\nYou take a look at your map.\n")
    for j in range(DUNGEON_ROWS):
        row = []
        for i in range(DUNGEON_COLS):
            if dungeon[i][j].visited == True:
                row.append(dungeon[i][j].name)
            else:
                row.append("unknown")
        print(row)
    return 

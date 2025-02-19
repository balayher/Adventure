from constants import *
from dungeon import create_dungeon

def main():
    dungeon = create_dungeon()
    print(dungeon[1][1].items)


main()
# A list of all the room descriptions.

def get_room_desc(room):
    match room.name:
        case "Armory":
            print("This room is filled with a variety of weapons and armor. Many seem dusty.")
        case "Kitchen":
            match room.prog:
                case 1:
                    print("You wonder if the chef is cooking more fish.")
                case _:
                    print("What smells so good? It seems like the chef is cooking up something tasty!")
        case "Hallway":
            print("A narrow corridor leads to an adjacent room to the West.")
        case "Foyer":
            print("The entrance to this place gives you the creeps. You can't wait to get out of here!")
        case _:
            print("You are in the void.")

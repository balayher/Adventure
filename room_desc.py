# A list of all the room descriptions.

def get_room_desc(room):
    match room.name:
        case "Kitchen":
            print("What smells so good? It seems like the chef is cooking up something tasty!")

        case "Dining Room":
            print("A spacious room that seems perfect for dinner time.")

        case "Closet":
            if room.prog == 0:
                print("It's pitch black in here!")
            else:
                print("The pantry is full of food.")

        case "Treasury":
            print("Many of Evan's valuables seem to be stored in here!")

        case "Dungeon":
            print("A drafty room used for holding people.")

        case "Hallway":
            print("A narrow corridor that connects the rooms to the north, west, and east.")

        case "Corridor":
            print("A small path that leads downstairs.")

        case "Lounge":
            print("A large room with plenty of seating. Perfect for relaxing.")

        case "Bathroom":
            print("A fancy looking restroom with chrome accessories.")

        case "Passageway":
            print("An uninteresting path that leads in four directions.")

        case "Gallery":
            print("Various art of all kinds are stored here. It's like a miniature museum.")

        case "Foyer":
            print("The entrance to this place gives you the creeps. You can't wait to get out of here!")

        case "Study":
            print("A quiet room used for work and reading.")

        case "Living Room":
            print("A cozy room designed for unwinding.")

        case "Armory":
            print("A room is filled with a variety of weapons and armor. Many seem dusty.")
        
        case "Exit":
            print("You've made it out of the mansion!")

        case _:
            print("You are in the void.")

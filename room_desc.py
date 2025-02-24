# A list of all the room descriptions.

def get_room_desc(room):
    match room.name:
        case "Kitchen":
            print("What smells so good? It seems like the CHEF is cooking up something tasty!")

        case "Dining Room":
            print("It's quite spacious and seems perfect for dinner time.")

        case "Closet":
            if room.prog == 0:
                print("It's pitch black in here!")
            else:
                print("This pantry is full of food.")

        case "Treasury":
            print("Many of Evan's valuables seem to be stored in here!")

        case "Dungeon":
            print("It's quite drafty. You're glad you aren't stuck here anymore.")

        case "Hallway":
            print("This area is narrow and connects the rooms to the North, East, and West.")

        case "Corridor":
            print("This narrow hallway leads downstairs.")

        case "Lounge":
            print("This large room has plenty of seating. It's perfect for relaxing!")

        case "Bathroom":
            print("With the tiled floor and chrome accessories, you feel as if you've walked into a hotel's restroom.")

        case "Passageway":
            print("This uninteresting path connects rooms in four directions.")

        case "Gallery":
            print("Various art of all kinds is stored here. It's like a miniature museum.")

        case "Foyer":
            print("The entrance to the mansion; your freedom is just ahead!")

        case "Study":
            print("This quiet room is ideal for working or reading.")

        case "Living Room":
            print("This room feels cozy. It seems perfect for unwinding after a long day.")

        case "Armory":
            print("A vast variety of weapons and armor coat the room. Many seem dusty and unkempt.")
        
        case "Exit":
            print("You've made it out of the mansion!")

        case _:
            print("You are in the void.")

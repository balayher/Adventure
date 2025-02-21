def inspect_room(room):
    # prints a brief description from looking around the current room
    # objects that can be interacted with are printed in CAPS
    # verifies item is in room before printing its message

    match room.name:
        case "Armory":
            print("The room is full of old weapons and armor that haven't seen much use recently.")
            if "Sword" in room.items:
                print("There's a recently polished SWORD in the corner of the room.")
            if "Shield" in room.items:
                print("A well crafted SHIELD sits above the mantle in the back.")

        case "Kitchen":
            print("The kitchen is well maintained, even while the CHEF cooks.")
            if "Knife" in room.items:
                print("A large chef's KNIFE is sitting on the counter.")
            if "Fish" in room.items:
                print("You notice a delicious looking FISH plated on the table.")

        case "Hallway":
            print("The hallway is quite narrow. A large metal DOOR leads to the West.")

        case "Foyer":
            print("The foyer gives you the chills. Part of you regrets coming in here.")
            if "Rug" in room.items:
                print("You see an ornate RUG in front of the entrance door.")
                
        case _:
            # if player ends up in an inaccessible room
            print("How did you get here?")

def inspect_room(room):
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
            print("How did you get here?")

def check_item(room, item, objects):
    if item not in room.items:
        print("That item is not in this room.")
        return False, ""

    match item:
        case "Sword":
            print("This steel sword seems like it can take down any guard.")
            if objects["Sword"].collect == True:
                objects["Sword"].inv = True
                return True, objects["Sword"].name
        case "Shield":
            print("The shield is mounted to the wall. It's just out of your reach.")
        case "Chef":
            match objects["Chef"].prog:
                case 0:
                    print("'You don't look familiar here. Are you a new friend to the Master?'")
                case _:
                    print("Dinner will be ready soon.")
        case "Knife":
            print("'If you know what's good for ya, you'll keep your hands off my knife!'")
        case "Fish":
            print("This red herring looks delicious!")
            if objects["Fish"].collect == True:
                objects["Fish"].inv = True
                return True, objects["Fish"].name
        case "Door":
            match objects["Door"].prog:
                case 0:
                    print("The door is locked.")
                case 1:
                    print("The door is open.")
                case _:
                    print("The door appears to be locked.")
        case "Rug":
            print("The ornate rug is quite beautiful.")

    return False, ""

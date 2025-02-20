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
                room.prog += 1
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

def use_item(inv, room, item, objects):
    if item not in inv:
        print("You do not possess that item.")
        return False

    match item:
        case "Sword":
            match room.name:
                case "Hallway":
                    print("You swing the sword at the door but it doesn't budge.")
                case _:
                    print("You swing the sword through the air, admiring its shine.")
        case "Fish":
            match room.name:
                case "Kitchen":
                    print("'No eating in ze kitchen!'")
                case _:
                    print("Feeling a bit hungry, you decide to eat the Red Herring.")
                    print("The fish was delicious, but you don't feel like you're any closer to your goal.")
                    objects["Fish"].inv = False
                    return True

    return False
def check_item(room, item, objects):
    if item not in room.items:
        print("That item is not in this room.")
        return

    match item:
        case "Sword":
            print("This steel sword seems like it can take down any guard.")
        case "Shield":
            print("The shield is mounted to the wall.")
        case "Chef":
            match objects["Chef"].prog:
                case 0:
                    print("'You don't look familiar here. Are you a new friend to the Master?'")
                case _:
                    print("Dinner will be ready soon.")
        case "Knife":
            print("The knife is in pristine shape. It's large enough to be used as a weapon.")
        case "Fish":
            print("This red herring looks delicious!")
        case "Door":
            match objects["Door"].prog:
                case 0:
                    print("The door is locked.")
                case 1:
                    print("The door is open.")
                case _:
                    print("The door appears to be locked.")
        case "Rug":
            match objects["Rug"].prog:
                case 0:
                    print("The ornate rug is quite beautiful. You wonder if there's something under it.")
                case 1:
                    print("The rug is slightly disheveled from your attempt to move it.")
                case 2:
                    print("The burnt remains of a once beautiful rug.")
                case _:
                    print("Seems there wasn't anything under here after all.")

    return

def take_item(room, item, objects):
    if item not in room.items:
        print("That item is not in this room.")
        return False, ""

    match item:
        case "Sword":
            if objects["Sword"].collect == True:
                print("The sword comes off the wall with ease.")
                objects["Sword"].inv = True
                return True, objects["Sword"].name
            print("It's stuck on the wall.")
        case "Shield":
            print("It's just out of your reach.")
        case "Chef":
            print("While you find the chef attractive, now is not the time!")
        case "Knife":
            print("'If you know what's good for ya, you'll keep your hands off my knife!'")
        case "Fish":
            if objects["Fish"].collect == True:
                print("Yum!")
                objects["Fish"].inv = True
                room.prog += 1
                return True, objects["Fish"].name
            print("The red herring is too hot to touch.")
        case "Door":
            match objects["Door"].prog:
                case 0:
                    print("You try to open the door but it's locked.")
                case 1:
                    print("The door is already open.")
                case _:
                    print("The door appears to be locked.")
        case "Rug":
            match objects["Rug"].prog:
                case 0:
                    print("You try to move the rug, but it appears to be bolted down. It won't move.")
                    objects["Rug"].prog = 1
                case 2:
                    print("You don't want to carry the evidence for your arson with you.")
                case _:
                    print("You've given up on the rug.")

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
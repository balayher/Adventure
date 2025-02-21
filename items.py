def check_item(player, room, item, objects):
    # checks if player is in the closet while it's dark
    if room.name == "Closet":
        if room.prog == 0:
            print("It's too dark to see anything.")
            return
    
    # corrects the reference if 'door' is used as a shorthand Celldoor or Metaldoor
    if item == "Door":
        if room.name == "Dungeon":
            item = "Celldoor"
        if room.name == "Gallery":
            item = "Metaldoor"

    # corrects the reference if 'goldcoin' is used rather than just 'coin'
    if item == "Goldcoin" or item == "Gold coin":
        item = "Coin"

    # checks if the item is in the player's inventory or in the room
    if item not in player.inv:
        if item not in room.items:
            print("That item is not in this room.")
            return

    # prints a description of the item in its current state
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
                    # after player tries to move the rug
                    print("The rug is slightly disheveled from your attempt to move it.")
                case 2:
                    # after player burns the rug
                    print("The burnt remains of a once beautiful rug.")
                case _:
                    print("Seems there wasn't anything under here after all.")

    return

def take_item(room, item, objects):
    # returns True & the item's name if the item is taken
    # this tells the function to remove the item from the room and add it to the player's inventory
    # returns False with no item name if it is not

    # checks if player is in the closet while it's dark
    if room.name == "Closet":
        if room.prog == 0:
            print("It's too dark to see anything.")
            return False, ""

    # corrects the reference if 'door' is used as a shorthand Celldoor or Metaldoor
    if item == "Door":
        if room.name == "Dungeon":
            item = "Celldoor"
        if room.name == "Gallery":
            item = "Metaldoor"

    # corrects the reference if 'goldcoin' is used rather than just 'coin'
    if item == "Goldcoin" or item == "Gold coin":
        item = "Coin"

    # checks if item is in the room
    if item not in room.items:
        print("That item is not in this room.")
        return False, ""

    # uses an item's 'collect' status to see if item is collectable
    # items that are never collectable are not checked
    match item:
        case "Sword":
            if objects["Sword"].collect == True:
                print("The sword comes off the wall with ease.")
                return True, item
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
                room.prog += 1
                return True, item
            print("The red herring is too hot to touch.")

        case "Door":
            match objects["Door"].prog:
                case 0:
                    print("You grab the door handle but it's locked.")
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
    # returns True if the item needs to be removed from the inventory
    # checks if the item is in your inventory
    if item not in inv:
        print("You do not possess that item.")
        return False

    # checks item with the current room to determine the effect of using
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
                    return True

    return False
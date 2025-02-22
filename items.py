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
        case "Handkerchief":
            print("You never leave home without it!")

        case "Chef":
            match objects["Chef"].prog:
                case 0:
                    print("'You don't look familiar. Are you a new friend of Evan's?'")
                case 1:
                    print(
                        "'You're looking for a code? Tell you what, help me out and I'll help you.'\n"
                        "'Bring me some broth from the pantry and I'll tell you the last digit!'"
                        )
                    objects["Cans"].prog == 1
                case 2:
                    print(f"'Like I said, the last digit is {self.code % 10}. Now let me cook!'")
                case _:
                    print("'Dinner will be ready soon.'")

        case "Knife":
            print("The knife is in pristine shape. It's large enough to be used as a weapon.")

        case "Fish":
            print("This red herring looks delicious!")

        case "Table":
            print("It's a mighty fine oak table.")

        case "Vase":
            match objects["Vase"].prog:
                case 0:
                    print("A pristine opal vase. You think this might be worth something!")
                case _:
                    print("A once pristine opal vase. You no longer think it's worth anything.")

        case "Bucket":
            match objects["Bucket"].prog:
                case 1:
                    print("The bucket is filled with water.")
                case _:
                    print("A sturdy wooden bucket.")

        case "Cans":
            print("Many cans of various food items.")



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


        case "Sword":
            print("This steel sword seems like it can take down any guard.")

        case "Shield":
            print("The shield is mounted to the wall.")

       

    return

def take_item(player, room, item, objects):
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
        case "Chef":
            print("While you find the chef attractive, now is not the time!")

        case "Knife":
            print("'If you know what's good for ya, you'll keep your hands off my knife!'")

        case "Fish":
            if objects["Fish"].collect == True:
                print("Yum!")
                return True, item
            print("The red herring is too hot to touch.")

        case "Table":
            print("Despite your desires to bring the table with you, it's simply too large.")

        case "Vase":
            if objects["Vase"].prog == 0:
                print("You attempt to pick up the vase, but it slips out of your hands and crashed on the ground.")
                objects["Vase"].prog += 1
            else:
                print("You don't want to cut yourself on the broken shards.")
        
        case "Bucket":
            print("You pick up the bucket.")
            return True, item

        case "Cans":
            match objects["Cans"].prog:
                case 0:
                    print("There's nothing tasty in these cans.")
                case 1:
                    print("You find the broth the Chef was looking for!")
                    objects["Cans"].prog += 1
                    return True, item
                case _:
                    print("You don't need any more of this.")



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

        case "Sword":
            if objects["Sword"].collect == True:
                print("The sword comes off the wall with ease.")
                return True, item
            print("It's stuck on the wall.")

        case "Shield":
            print("It's just out of your reach.")


    return False, ""

def use_item(player, room, item, objects):
    # returns True if the item needs to be removed from the inventory
    # checks if the item is in your inventory
    if item not in player.inv:
        print("You do not possess that item.")
        return False

    # checks item with the current room to determine the effect of using
    match item:
        case "Handkerchief":
            match room.name:
                case "Armory":
                    print(
                        "You try to wipe away the dirt on the armor, but it's caked on pretty heavily.\n"
                        "Perhaps you could use something else to clean it?"
                    )
                case "Bathroom":
                    print("You don't want to get your handkerchief wet")
                case _:
                    print("You aren't sure how a handkerchief helps out here.")

        case "Fish":
            match room.name:
                case "Kitchen":
                    print("'No eating in the kitchen!'")
                case _:
                    print("Feeling a bit hungry, you decide to eat the Red Herring.")
                    print("The fish was delicious, but you don't feel like you're any closer to your goal.")
                    return True

        case "Bucket":
            match room.name:
                case "Bathroom":
                    if objects["Bucket"].prog == 0:
                        if objects["Sink"].prog == 1 or objects["Shower"].prog == 1:
                            print("You fill the bucket with water.")
                            objects["Bucket"].prog = 1
                        else:
                            print("You should turn on the water first!")
                    else:
                        print("The bucket is already full of water.")

                case "Living Room":
                    if objects["Bucket"].prog == 1:
                        if objects["Fireplace"].prog == 0:
                            print(
                            "You use the water to put out the fire.\n"
                            "You notice a small KEY in the back of the fireplace."
                            )
                            objects["Bucket"].prog = 0
                            objects["Fireplace"].prog = 1
                            room.items.remove("Fireplace")
                            room.items.add("Key")
                        else:
                            print("The fire is already out.")
                    else:
                        print("You don't want to put the bucket in the fireplace.")
                            
                case _:
                    print("You aren't sure how the bucket helps here.")

        case "Cans":
            match room.name:
                case "Kitchen":
                    print(
                        "'Yes! This is what I needed for the soup!'\n"
                        f"'The last digit of the code is {self.code % 10}.\n"
                        "Now leave me alone!"
                    )
                    objects["Chef"].prog += 1
                    return True
                case _:
                    print("This doesn't help you here.")


        case "Sword":
            match room.name:
                case "Hallway":
                    print("You swing the sword at the door but it doesn't budge.")
                case _:
                    print("You swing the sword through the air, admiring its shine.")

       

    return False
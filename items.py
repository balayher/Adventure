import time

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
                # after reading the diary
                case 1:
                    print(
                        "'You're looking for a code? Tell you what, help me out and I'll help you.'\n"
                        "'Bring me some broth from the pantry and I'll tell you the last digit!'"
                        )
                    objects["Cans"].prog == 1
                # after given the chef the cans of broth
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
            if objects["Vase"].prog == 0:
                print("A pristine opal vase. You think this might be worth something!")
            # after breaking the vase
            else:
                print("A once pristine opal vase. You no longer think it's worth anything.")

        case "Bucket":
            # while bucket is filled with water
            if objects["Bucket"].prog == 1:
                print("The bucket is filled with water.")
            else:
                print("A sturdy wooden bucket.")

        case "Cans":
            print("Many cans of various food items.")

        case "Rice":
            print("A giant bag of rice.")

        case "Safe":
            if objects["Safe"].prog == 0:
                print(
                    "A sturdy metal safe. There must be something good inside!\n"
                    "There is a keypad on the front."
                )
            else:
                print("The safe is open.")

        case "Keyring":
            print("A set of keys hangs on the wall above the safe.")

        case "Brain":
            print(
                "You aren't sure if it's made of gold or is a real brain plated in gold.\n"
                "The thought gives you the creeps."
            )

        case "Celldoor":
            print("The metal door to your cell.")

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

        case "Coin":
            print("A gold coin.")

        case "Clock":
            print(f"The current time is {time.strftime("%H:%M:%S")}.")

        case "Chair":
            print("A comfy looking chair. Big enough to fit one and a half people.")

        case "Sofa":
            print("A comfy looking sofa. Big enough to fit three people, four if you squeeze in.")

        case "Diary":
            # displays the first part of the diary only on first read
            if objects["Diary"].prog == 0:
                objects["Diary"].prog = 1
                objects["Chef"].prog = 1
                print(
                    "You open up the diary and begin to read...\n\n"
                    "Yesterday I took Roary to the aviary looking for his favorite birds.\n"
                    "They weren't too pleased that I brought him; they said no lions allowed.\n"
                    "Of course a little bit of green changed their mind.\n"
                    "The golden conure was a thing of beauty! I would love one of my own someday.\n"
                    "Roary in particular loved the cockatoo. I don't think it recipricated the feelings.\n\n"
                    "You turn a few more pages until you find something interesting...\n"
                    )
                input("Press Enter to continue...")
                print(
                    "\nMy precious is secure in the safe. I've given myself hints so I don't forget the code.\n"
                    "The first digit is hidden in my favorite painting.\n"
                    "The second digit is inscribed on my grandfather's armor.\n"
                    "The third digit is printed on the back of my favorite book.\n"
                    "The final digit was given only to my trusted friends.\n"
                    "Only by inputting all four digits can you open the safe. No one will ever figure it out!"
                )
                if item not in player.inv:
                    print("\nThis seems too important to leave behind.")
                    player.inv.add(item)
                    room.items.remove(item)
                    print(f"You add the {item} to your inventory.") 
            else:
                # checks if any digits have been found and displays the ones that have
                print(
                    "My precious is secure in the safe. I've given myself hints so I don't forget the code.\n"
                    "The first digit is hidden in my favorite painting."
                )
                if objects["Diary"].prog % 4 // 2 == 1:
                    print(player.code // 1000)
                print("The second digit is inscribed on my grandfather's armor.")
                if objects["Diary"].prog % 8 // 4 == 1:
                    print(player.code % 1000 // 100)
                print("The third digit is printed on the back of my favorite book.")
                if objects["Diary"].prog % 16 // 8 == 1:
                    print(player.code % 100 // 10)
                print("The final digit was given only to my trusted friends.")
                if objects["Diary"].prog // 16 == 1:
                    print(player.code % 100 // 10)
                print("Only by inputting all four digits can you open the safe. No one will ever figure it out!")

        case "Sink":
            if objects["Sink"].prog == 1:
                print("The sink is running...")
            else:
                print("An ordinary sink.")

        case "Toilet":
            print("You wonder if there's something hidden inside, but you don't want to find out.")

        case "Shower":
            if objects["Shower"].prog == 1:
                print("The shower is running...")
            else:
                if objects["Soap"].prog == 0:
                    print("You see a bar of SOAP hidden in the shower.")
                    objects["Soap"].prog = 1
                    room.inv.add("Soap")
                else:
                    print("A walk-in shower.")

        case "Soap":
            print("A basic bar of soap.")

        case "Door":
            print("A wooden door.")

        case "Statue":
            print("It's a giant statue of some sort of parakeet.")

        case "Painting":
            print("It's a painting of a lion surrounded by birds.")
            # checks if diary has been read
            if objects["Diary"].prog > 0:
                print(f"Upon further inspection, you notice a small {player.code // 1000} in the corner.")
                # adds digit to diary if it's not already there
                if objects["Painting"].prog == 0:
                    objects["Painting"].prog += 1
                    objects["Diary"].prog += 2
                    print("You note it down in the DIARY")

        case "Metaldoor":
            print("A large metal door. There must be something important in this room.")


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
                room.prog += 1
            # after vase is broken
            else:
                print("You don't want to cut yourself on the broken shards.")
        
        case "Bucket":
            print("You pick up the bucket.")
            return True, item

        case "Cans":
            match objects["Cans"].prog:
                case 0:
                    print("There's nothing tasty in these cans.")
                # after the chef asks for broth
                case 1:
                    print("You find the broth the Chef was looking for!")
                    objects["Cans"].prog += 1
                    return True, item
                case _:
                    print("You don't need any more of this.")

        case "Rice":
            print("You can barely move the top bag.")

        case "Safe":
            if objects["Safe"].prog == 0:
                s = input("What is the code? ")
                # checks that the player input a number, then checks it with the safe code
                if s.isdigit():
                    code = int(s)
                    if code == player.code:
                        print("The safe opens! You look inside to find a golden BRAIN!")
                        return True, "Brain"
                    else:
                        print("Incorrect code.")
                else:
                    print("There are only numbers on the keypad.")
            # after opening the safe
            else:
                print("The safe is open.")

        case "Keyring":
            print("It's too high to reach!")

        case "Celldoor":
            if objects["Celldoor"].prog == 0:
                print(
                    "You pull the celldoor open with ease.\n"
                    "Seems whoever put you in here forgot to lock it!"
                )
                objects["Celldoor"].prog += 1
                room.exits[2] = True
            # after opening the door
            else:
                print("The door is already open.")

        case "Rug":
            match objects["Rug"].prog:
                case 0:
                    print("You try to move the rug, but it appears to be bolted down. It won't move.")
                    objects["Rug"].prog = 1
                # after burning the rug
                case 2:
                    print("You don't want to carry the evidence for your arson with you.")
                case _:
                    print("You've given up on the rug.")

        case "Clock":
            print("It's out of reach.")

        case "Chair":
            if objects["Chair"].prog == 0:
                print(
                "You take a seat and begin to relax.\n"
                "After a couple minutes, you get back up. You don't want to fall asleep."
                )
                objects["Chair"].prog += 1
            else:
                print("You don't want to risk falling asleep.")

        case "Sofa":
            if objects["Sofa"].prog == 0:
                print(
                "You lie down on the sofa and stare at the ceiling.\n"
                "You ponder if this burglary thing is such a good idea after all.\n"
                "Eventually, you get up. You don't want to fall asleep here."
                )
                objects["Sofa"].prog += 1
            else:
                print("You don't want to risk falling asleep.")

        case "Diary":
            if objects["Diary"].collect == True:
                return True, item
            print("You aren't a fan of birds.")

        case "Sink":
            if objects["Sink"].prog == 0:
                print("You turn on the sink.")
                objects["Sink"].prog = 1
            else:
                print("You turn off the sink.")
                objects["Sink"].prog = 0

        case "Toilet":
            print(
                "When you gotta go you gotta go!\n\n"
                "You flush when you're finished."
                )

        case "Shower":
            if objects["Shower"].prog == 0:
                print("You turn on the shower.")
                objects["Shower"].prog = 1
            else:
                print("You turn off the shower.")
                objects["Shower"].prog = 0

        case "Soap":
            return True, item

        case "Door":
            print("You try to open the wooden door but it's locked.")

        case "Statue":
            print("The statue is much too heavy to move.")

        case "Painting":
            print("Ever since the 'McCloud Incident', you've stayed away from paintings.")

        case "Metaldoor":
            print("You try to open the metal door but it's locked.")


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
                    # checks if bucket is empty and that either the sink or shower is running
                    if objects["Bucket"].prog == 0:
                        if objects["Sink"].prog == 1 or objects["Shower"].prog == 1:
                            print("You fill the bucket with water.")
                            objects["Bucket"].prog = 1
                        else:
                            print("You should turn on the water first!")
                    else:
                        print("The bucket is already full of water.")

                case "Living Room":
                    # checks if bucket has water and the fireplace has fire
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

        case "Keyring":
            match room.name:
                case "Gallery":
                    print("The metal door unlocks! With a bit of effort you open it up.")
                    room.items.remove("Metaldoor")
                    return True
                case "Treasury":
                    print("The safe requires a keycode, not a key.")
                case _:
                    print("Nothing looks unlockable in here.")

        case "Brain":
            match room.name:
                case "Foyer":
                    # checks if guard is there before offering the brain to the guard
                    if "Guard" in room.items:
                        print(
                            "'Is this Evan's prized possession? I bet it's worth a fortune!'\n"
                            "'If you hand it over, I'll let you through.'"
                            )
                        s = input("'What do you say?' ").lower()
                        if s == "yes" or s == "y":
                            print("'Thanks! I'm out of here!")
                            objects["Guard"].prog = 3
                            room.exits[1] = True
                            room.items.remove("Guard")
                            return True
                        print("'If you change your mind, let me know.'")
                    else:
                        print("What are you going to do with that?")
                case "Kitchen":
                    print("That's Evan's prized possession! He won't be happy with you...")
                case _:
                    print("What are you going to do with that?")

        case "Coin":
            match room.name:
                case "Foyer":
                    # checks if guard is there before offering the coin to the guard
                    # will not offer coin if the diary hasn't been read yet
                    if "Guard" in room.items and objects["Diary"].prog > 0:
                        print(
                            "'A gold coin? That's not enough of a bribe to let you out.'\n"
                            "'If you hand it over though, I'll tell you the last digit to the safe.'"
                            )
                        s = input("'What do you say?' ").lower()
                        if s == "yes" or s == "y":
                            print(f"'Thanks! The last digit is {self.code %10}.'")
                            objects["Guard"].prog = 1
                            return True
                        print("'If you change your mind, let me know.'")
                    else:
                        print("The coin's shiny, but not useful here.")
                case "Kitchen":
                    print("You don't need to pay me for dinner!")
                case _:
                    print("The coin's shiny, but not useful here.")

        case "Diary":
            # reads diary (same as if checking the diary)
            check_item(player, room, item, objects)

        case "Soap":
            match room.name:
                case "Armory":
                    # cleans the armor, revealing the 3rd digit to the safe code
                    print(
                        "You use the soap to scrub all the dirt off of the armor.\n"
                        "You wipe the remains away with your handkerchief.\n"
                        f"Underneath you find a {player.code % 100 // 10} engraved on the armor.\n"
                        "You note it down in the DIARY."
                        )
                    player.inv.remove("Handkerchief")
                    objects["Armor"].prog += 1
                    objects["Diary"].prog += 8
                    return True
                case _:
                    print("Nothing needs cleaning here.")


        case "Sword":
            match room.name:
                case "Hallway":
                    print("You swing the sword at the door but it doesn't budge.")
                case _:
                    print("You swing the sword through the air, admiring its shine.")

       

    return False
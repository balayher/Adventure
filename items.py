import time
from alias import item_alias

def check_item(player, room, item, objects):
    # checks if player is in the closet while it's dark
    if room.name == "Closet":
        if room.prog == 0:
            print("It's too dark to see anything.")
            return
    
    # corrects the player's input to a referenceable item, if applicable
    item = item_alias(item, room)

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
                        "'You want info about a code? Tell you what, help me out and I'll help you.'\n"
                        "'Bring me some broth from the pantry and I'll tell you the last digit of the code!'"
                        )
                    objects["Cans"].prog = 1
                # after given the chef the cans of broth
                case 2:
                    print(f"'Like I said, the last digit is {player.code % 10}. Now let me cook!'")
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
            if objects["Keyring"].prog == 0:
                print("A set of keys hangs on the wall above the safe.")
            else:
                print("These keys could unlock anything in the mansion.")

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
            print(f'The current time is {time.strftime("%H:%M:%S")}.')

        case "Chair":
            print("A comfy looking chair. There's enough room to fit one and a half people.")

        case "Sofa":
            print("A comfy looking sofa. It's big enough to fit three, maybe four people if you squeeze in.")

        case "Diary":
            # displays the first part of the diary hasn't been read
            if objects["Diary"].prog == 0:
                print("A worn notebook that says 'Evan's Diary: DO NOT READ' on the front.")
            else:
                # checks if any digits have been found and displays the ones that have
                # prog has +2 for first digit, +4 for second, +8 for third, and +16 for last
                print("The first digit is hidden within my favorite painting.")
                if objects["Diary"].prog % 4 // 2 == 1:
                    print(player.code // 1000)
                print("The second digit is engraved on my grandfather's armor.")
                if objects["Diary"].prog % 8 // 4 == 1:
                    print(player.code % 1000 // 100)
                print("The third digit is inscribed on the back of my favorite book.")
                if objects["Diary"].prog % 16 // 8 == 1:
                    print(player.code % 100 // 10)
                print("The final digit was given only to my trusted friends.")
                if objects["Diary"].prog // 16 == 1:
                    print(player.code % 10)

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
                    player.inv.add("Soap")
                    print(f"You add the Soap to your inventory.")
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
                    print("You note it down in the DIARY.")

        case "Metaldoor":
            print("A large metal door. There must be something important behind it.")

        case "Guard":
            match objects["Guard"].prog:
                case 0:
                    print("A burly guard is blocking the exit.")
                # after trying to fight the guard
                case 1:
                    print("The guard was stronger than you thought. You wonder if you can bribe them.")
                # after giving them the gold coin
                case 2:
                    print(f"'I told you the last digit was {player.code % 10}. Bring me the goods if you want to leave!'")
                case _:
                    print("The guard was no where to be seen.")

        case "Stick":
            print("A long wooden stick.")

        case "Books":
            print("There are various books about exotic birds on the desk.")
            # checks if diary has been read
            if objects["Diary"].prog > 0:
                print(
                    "You flip over the one titled 'Flight of the Golden Conure'.\n"
                    f"You find the number {(player.code % 100) // 10} inscribed on the back."
                )
                # adds digit to diary if it's not already there
                if objects["Books"].prog < 4:
                    objects["Books"].prog += 4
                    objects["Diary"].prog += 8
                    print("You note it down in the DIARY.")

        case "Candle":
            # while candle is lit
            if objects["Candle"].prog == 1:
                print("The candle burns brightly.")
            else:
                print("An unscented candle.")

        case "Tv":
            print("The television is turned off.")

        case "Remote":
            print("This remote should turn on the tv.")

        case "Fireplace":
            # checks if fireplace has fire
            if objects["Fireplace"].prog == 0:
                print("The fire warms up the room. You think you see something shiny behind the flames...")
            else:
                print("The room is colder now that the flames are out.")

        case "Key":
            print("A small house key.")

        case "Sword":
            print("This steel sword seems like it can take down any guard.")

        case "Shield":
            print("The shield is mounted to the wall.")

        case "Armor":
            # checks if armor is dirty
            if objects["Armor"].prog == 0:
                print("This once proud armor is coated in dirt and grime.")
            else:
                print(f"You find a {player.code % 1000 // 100} engraved on the armor.")
                if objects["Diary"].prog % 8 // 4 == 0:
                    print("You note it down in the DIARY.")
                    objects["Diary"].prog += 4
       
    return

def take_item(player, room, item, objects):
    # returns True & the item's name if the item is taken
    # this tells the function to remove the item from the room and add it to the player's inventory
    # returns False with no item name if it is not

    # corrects the player's input to a referenceable item, if applicable
    item = item_alias(item, room)

    # checks if player is in the closet while it's dark
    if room.name == "Closet" and item != "Candle":
        if room.prog == 0:
            print("It's too dark to see anything.")
            return False, ""

    # checks if item is in the room, if not checks if item is in player's inventory
    # if in player's inventory, calls use instead
    if item not in room.items:
        if item in player.inv:
            remove, item = use_item(player, room, item, objects)
            if remove == True:
                player.inv.remove(item)
        else:
            print("That item is not in this room.")
        return False, ""

    # uses an item's 'collect' status to see if item is collectable
    # items that are never collectable are not checked
    match item:
        case "Chef":
            check_item(player, room, item, objects)

        case "Knife":
            print("'If you know what's good for ya, you'll keep your hands off my knife!'")

        case "Fish":
            print("Yum!")
            return True, item

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
            return True, item

        case "Cans":
            match objects["Cans"].prog:
                case 0:
                    print("There's nothing tasty in these cans.")
                # after the chef asks for broth
                case 1:
                    print("You find the broth the Chef was looking for!")
                    objects["Cans"].prog += 1
                    player.inv.add(item)
                    print(f"You add the {item} to your inventory.")
                case _:
                    print("You don't need any more of these.")

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
                        player.inv.add("Brain")
                        objects["Safe"].prog = 1
                        print(f"You add the Brain to your inventory.")
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
                    "You push the celldoor open with ease.\n"
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
                    print("You don't want to carry the evidence of your arson with you.")
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
            objects["Diary"].prog = 1
            objects["Chef"].prog = 1
            print(
                "You open up the diary and begin to read...\n\n"
                "Yesterday I took Roary to the aviary, looking for his favorite birds.\n"
                "They weren't too pleased that I brought him: they said no lions allowed.\n"
                "Of course a little bit of green changed their mind.\n"
                "The golden conure was a thing of beauty! I would love one of my own someday.\n"
                "Roary in particular loved the cockatoo. I don't think it recipricated the feelings.\n\n"
                "You turn a few more pages until you find something interesting...\n"
            )
            input("Press Enter to continue...")
            print(
                "\nMy precious is secure in the safe. I've given myself hints so I don't forget the code.\n"
                "The first digit is hidden within my favorite painting.\n"
                "The second digit is engraved on my grandfather's armor.\n"
                "The third digit is inscribed on the back of my favorite book.\n"
                "The final digit was given only to my trusted friends.\n"
                "The safe will only open once the full code is entered. No one will ever figure it out!"
            )
            print("\nThis seems too important to leave behind.")
            return True, item

        case "Sink":
            if objects["Sink"].prog == 0:
                print("You turn on the sink.")
                objects["Sink"].prog = 1
            else:
                print("You turn off the sink.")
                objects["Sink"].prog = 0

        case "Toilet":
            print(
                "When you gotta go, you gotta go!\n"
                "You flush the toilet when you're finished."
            )

        case "Shower":
            if objects["Shower"].prog == 0:
                print("You turn on the shower.")
                objects["Shower"].prog = 1
            else:
                print("You turn off the shower.")
                objects["Shower"].prog = 0

        case "Door":
            if objects["Door"].prog == 0:
                print("You try to open the wooden door but it's locked.")
            else:
                print("The door is already open.")

        case "Statue":
            print("The statue is much too heavy to move.")

        case "Painting":
            print("Ever since the 'Lizard Incident', you've stayed away from paintings.")
            if objects["Diary"].prog > 0:
                print(f"Upon further inspection, you notice a small {player.code // 1000} in the corner.")
                # adds digit to diary if it's not already there
                if objects["Painting"].prog == 0:
                    objects["Painting"].prog += 1
                    objects["Diary"].prog += 2
                    print("You note it down in the DIARY.")

        case "Metaldoor":
            if objects["Metaldoor"].prog == 0:
                print("You try to open the metal door but it's locked.")
            else:
                print("The door is already open.")

        case "Guard":
            match objects["Guard"].prog:
                case 0:
                    print(
                        "You try to take a swing at the guard, but he swiftly knock you to the ground.\n"
                        "'Try that again and I'll stick Roary on ya!'"
                    )
                    objects["Guard"].prog = 1
                # after trying to fight the guard
                case 1:
                    print("You aren't in a hurry to find out who Roary is...")
                # after giving the guard the gold coin
                case 2:
                    print("Seems you'll need a better bribe or a weapon to get through the guard.")
                case _:
                    print("The guard was no where to be seen.")

        case "Stick":
            return True, item

        case "Books":
            if objects["Diary"].prog > 0 and objects["Books"].prog < 4:
                print(
                    "You flip over the book 'Flight of the Golden Conure'.\n"
                    f"The number {(player.code % 100) // 10} is inscribed on the back."
                )
                objects["Books"].prog += 4
                objects["Diary"].prog += 8
                print("You note it down in the DIARY.")
            else:
                book = objects["Books"].prog % 4
                match book:
                    case 0:
                        print(
                            "'Flight of the Golden Conure'\n\n"
                            "The conure's brilliant yellow feathers glisten in the sun's rays.\n"
                            "Their verdant remiges contrast beautifully with the golden hue of their wings.\n"
                            "The golden conure hears trouble and races back to defend their nest.\n"
                            "They join their fellow conures as they fight off a toucan seeking to feed on their eggs.\n"
                            "Truly a marvel to behold!"
                        )
                        objects["Books"].prog += 1
                    case 1:
                        print(
                            "'Whatcha Do, Cockatoo?'\n\n"
                            "Cocaktoos frequently preen throughout the day to maintain their plumage.\n"
                            "They will assist each other in preening the hard to reach feathers.\n"
                            "In addition, their vocalisations tend to be loud and harsh.\n"
                            "Palm cockatoos are known to communicate by drumming on branches with a stick.\n"
                            "Rumor has it that they were the inspiration behind a 2017 baseball scandal."
                        )
                        objects["Books"].prog += 1
                    case 2:
                        print(
                            "'Three Cards and a Dream: The Mute Swan Saga'\n\n"
                            "Tensions were rising at the table. The game was getting intense.\n"
                            "The combination of Mute Swan, Maned Duck, and Gray Catbird seemed strong on the surface.\n"
                            "In reality, the lack of additional card draw limited its potential.\n"
                            "Knowing things were getting dire, Vik tucked her last card under the Mute Swan, hoping for the best.\n"
                            "Fortunately, her savior had arrived: the Savi's Warbler.\n"
                            "With her water engine fully online, nothing would stop Vik now!"
                        )
                        objects["Books"].prog += 1
                    case 3:
                        print(
                            "'Lions on the Hunt'\n\n"
                            "Lions typically hunt medium to large sized ungulates.\n"
                            "They are also known to steal the kills of other predators, especially hyenas.\n"
                            "After all, why spend energy killing your prey when you can find readily available food?\n"
                            "An adult lioness requires roughly 11 lbs of meat per day while a male requires about 15 lbs.\n"
                            "Lions will gorge themselves after a kill, consuming upwards of 60 lbs of meat at a time.\n"
                            "If they can't finish their kill in one session, they'll take a break and return to it in a few hours."
                        )
                        objects["Books"].prog -= 3
                    case _:
                        print("You've read all these before.")

        case "Candle":
            return True, item

        case "Tv":
            print("You attempt to turn the tv on, but none of the accessible buttons seem to work.")

        case "Remote":
            print("The remote doesn't work. Looks like it's out of batteries.")

        case "Fireplace":
            # checks if fireplace has fire
            if objects["Fireplace"].prog == 0:
                print("It's too hot to touch!")
            else:
                print("You wonder if you should rekindle the fire.")

        case "Sword":
            print("The sword comes off the wall with ease.")
            return True, item

        case "Shield":
            print("It's just out of your reach.")

        case "Armor":
            print("It's not your size.")

    return False, ""

def use_item(player, room, item, objects):
    # returns True if the item needs to be removed from the inventory

    # corrects the player's input to a referenceable item, if applicable
    item = item_alias(item, room)

    # checks if the item is in player's inventory, if not checks if in the room
    # if in the room, calls take_item instead
    if item not in player.inv:
        if item in room.items:
            take, item = take_item(player, room, item, objects)
            if take == True:
                player.inv.add(item)
                room.items.remove(item)
                print(f"You add the {item} to your inventory.") 
        else:
            print("You do not possess that item.")
        return False, item

    # checks item with the current room to determine the effect of using
    match item:
        case "Handkerchief":
            match room.name:
                case "Armory":
                    print(
                        "You try to wipe away the dirt off of the armor, but it's caked on pretty heavily.\n"
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
                    return True, item

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
                            room.prog += 1
                            player.inv.add("Key")
                            print(f"You add the Key to your inventory.")
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
                        "'Yes! This is just what I needed for my soup!'\n"
                        f"'The last digit of the code is {player.code % 10}.'\n"
                        "'Now leave me alone!'"
                    )
                    # adds digit to diary if it's not already there
                    if objects["Diary"].prog < 16:
                        objects["Diary"].prog += 16
                        print("You note the digit down in the DIARY.")
                    objects["Chef"].prog += 1
                    return True, item

                case _:
                    print("This doesn't help you here.")

        case "Keyring":
            match room.name:
                case "Gallery":
                    print("The metal door unlocks! With a bit of effort you open it up.")
                    objects["Metaldoor"].prog = 1
                    room.exits[1] = True
                    return True, item

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
                            print("'Thanks! I'm out of here!'")
                            objects["Guard"].prog = 4
                            room.exits[1] = True
                            room.items.remove("Guard")
                            return True, item
                        print("'If you change your mind, let me know.'")
                    else:
                        print("What are you going to do with that?")

                case "Kitchen":
                    print("'That's Evan's prized possession! He won't be happy with you...'")

                case _:
                    print("What are you going to do with that?")

        case "Coin":
            match room.name:
                case "Foyer":
                    # checks if guard is there before offering the coin to the guard
                    # will not offer coin if the diary hasn't been read yet
                    if "Guard" in room.items and objects["Diary"].prog > 0:
                        print(
                            "'A gold coin? You think you can bribe me with that?!'\n"
                            "'I'd need something worth more than that if you want out of here.'\n"
                            "'Bring me something out of the safe and then we can talk.'\n"
                            "'I'll even tell you the last digit to the safe, if you give me the coin.'"
                            )
                        s = input("'What do you say?' ").lower()
                        if s == "yes" or s == "y":
                            print(f"'Thanks! The last digit is {player.code %10}.'")
                            objects["Guard"].prog = 2
                            if objects["Diary"].prog < 16:
                                objects["Diary"].prog += 16
                                print("You note the digit down in the DIARY")
                            return True, item
                        print("'If you change your mind, let me know.'")
                    else:
                        print("The coin's shiny, but not useful here.")

                case "Kitchen":
                    print("'You don't need to pay me for dinner!'")

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
                        f"Underneath you find a {player.code % 1000 // 100} engraved on the armor.\n"
                    )
                    if objects["Diary"].prog == 0:
                        print("You aren't sure what that means, but it seems important.")
                    else:
                        print("You note it down in the DIARY.")
                        objects["Diary"].prog += 4
                    player.inv.remove("Handkerchief")
                    objects["Armor"].prog += 1
                    
                    return True, item

                case _:
                    print("Nothing needs cleaning here.")

        case "Stick":
            match room.name:
                case "Foyer":
                    # checks if guard is in the room
                    if "Guard" in room.items:
                        print("'That flimsy thing will break in half if you try to swing it at me!")
                    else:
                        print("You're certain this stick is useful something, but you can't figure out what.")

                case "Treasury":
                    # checks if keyring is in the room
                    if "Keyring" in room.items:
                        print("You manage to hook the keyring off the wall and bring it to you.")
                        player.inv.add("Keyring")
                        room.items.remove("Keyring")
                        print(f"You add the Keyring to your inventory.")
                        objects["Stick"].prog = 1
                        objects["Keyring"].prog = 1
                    else:
                        print("You've already gotten the keyring.")

                case "Corridor":
                    print("You could reach the clock, but you don't want to damage it.")

                case "Armory":
                    print("You try to knock the shield off the wall, but to no avail.")
                 
                case "Dining Room":
                    if objects["Vase"].prog == 0:
                        print(
                            "You swing the stick around and knock the vase over.\n"
                            "It shatters into pieces."
                        )
                        objects["Vase"].prog += 1
                        room.prog += 1
                    else:
                        print("Haven't you done enough damage for one day?")
                 
                case "Living Room":
                    if objects["Stick"].prog == 0:
                        print(
                            "You resist the urge to throw the stick into the fireplace.\n"
                            "You feel like you need it for something..."
                        )
                    else:
                        print("You toss the stick into the fireplace.")
                        return True, item

                case "Gallery":
                    print("You don't want to damage anything in here.")
                 
                case _:
                    print("You're certain this stick is useful something, but you can't figure out what.")

        case "Candle":
            # before candle is lit
            if objects["Candle"].prog == 0:
                match room.name:
                    #lights the candle
                    case "Living Room":
                        print("You light the candle with the flames of the fireplace.")
                        objects["Candle"].prog = 1
                    
                    case _:
                        print("There's nothing to light the candle with here.")
            
            # when candle is lit
            else:
                match room.name:
                    case "Living Room":
                        print("The candle's already lit.")
                    
                    case "Closet":
                        # lights up the closet
                        if room.prog == 0:
                            room.prog += 1
                            print(
                                "Illuminating the darkness, you see that this closet is actually a food pantry.\n"
                                "The shelves are fully stocked with various CANS of food.\n"
                                "Some large bags of RICE are piled off to the side.\n"
                                "A wooden BUCKET sits inconspicuously in the corner."
                            )
                        else:
                            print("You can already see in here.")

                    case "Gallery":
                        print("You don't want to damage the painting.")

                    case "Hallway":
                        # sets the rug on fire
                        if objects["Rug"].prog < 2:
                            print(
                                "You set the rug ablaze! You're impressed by how fast it burns.\n"
                                "When the flames abet, you find a gold COIN underneath."
                            )
                            objects["Rug"].prog = 2
                            room.prog = 1
                            player.inv.add("Coin")
                            print(f"You add the Coin to your inventory.")
                        else:
                            print("You've done enough damage here.")

                    case _:
                        print("Nothing flamable here.")

        case "Key":
            match room.name:
                case "Passageway":
                    print("You unlock the door!")
                    objects["Door"].prog = 1
                    room.exits[2] = True
                    return True, item
                
                case _:
                    print("There's nothing to unlock here.")

        case "Sword":
            match room.name:
                case "Kitchen":
                    print("'Be careful where you're swinging that thing!'")

                case "Foyer":
                    # checks if guard is there before offering the brain to the guard
                    if "Guard" in room.items:
                        print(
                            "'Whoa now, let's not get too hasty here! (I don't get paid enough for this...)'\n"
                            "'You're free to go. I'd take Evan's scolding over getting maimed by a sword any day.'\n"
                            "The guard leaves."
                        )
                        objects["Guard"].prog = 3
                        room.exits[1] = True
                        room.items.remove("Guard")
                        
                    else:
                        print("The guard is already gone.")

                case _:
                    print("You brandish the sword, admiring its shine.")

    return False, item
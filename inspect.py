def inspect_room(room):
    # prints a brief description from looking around the current room
    # objects that can be interacted with are printed in CAPS
    # verifies item is in room before printing its message

    match room.name:
        case "Kitchen":
            print(
                "The kitchen is well maintained, even while the CHEF cooks.\n"
                "A large chef's KNIFE is sitting on the counter."
            )
            if "Fish" in room.items:
                print("You notice a delicious looking FISH plated on the table.")
            print("The Dining Room to the South is the only connecting room here.")

        case "Dining Room":
            print("The giant TABLE in the center of the room has seating for 8 guests.")
            if room.prog == 0:
                print("You notice an expensive looking VASE in the corner.")
            else:
                print("The shards of a now broken VASE are scattered about the room.")
            print("There appear to be rooms to the North, East, and South.")

        case "Closet":
            if room.prog == 0:
                print("It's pitch black in here! Better return to the Dining Room to the North.")
            else:
                print(
                    "The pantry is overloaded with foodstuffs.\n"
                    "The shelves are fully stocked with various CANS of food.\n"
                    "Some large bags of RICE are piled off to the side."
                )
                if "Bucket" in room.items:
                    print("A wooden BUCKET sits inconspicuously in the corner.")
                print("The Dining Room to the North is still the only way out.")

        case "Treasury":
            print(
                "Upon further inspection, there seems to be fewer valuables than anticipated.\n"
                "All the good stuff appears to be stored inside the SAFE in the center of the room."
            )
            if "Keyring" in room.items:
                print("A nondescript KEYRING sits on a hook well above the SAFE.")
            print("Returning East to the Lounge is the only way out.")

        case "Dungeon":
            print(
                "The concrete walls are uninviting. Someone drew something naughty in the corner.\n"
                "The CELLDOOR is the only thing between a captive and the room to the South."
            )

        case "Hallway":
            print("This hallway links the rooms to the North, East, and West")
            if room.prog == 0:
                print("A beautiful RUG adds some color to an otherwise lifeless room.")
            else:
                print("The burnt remains of the RUG is the only notable thing in here.")

        case "Corridor":
            print(
                "This corridor links the Gallery to the East to the Lounge downstairs to the South.\n"
                "A silver CLOCK hangs on the wall."
            )

        case "Lounge":
            print(
                "Unlike most lounges, there are no signs of smoke anywhere.\n"
                "A large SOFA and a comfy looking CHAIR decorate the room."
            )
            if "Diary" in room.items:
                print("Someone left a DIARY on the armrest of the CHAIR. Could it be Evan's?")
            print("There are rooms to the East and West as well a staircase leading to the North.")

        case "Bathroom":
            print(
                "This reminds you of a fancy hotel restroom.\n"
                "The TOILET looks clean enough to eat off of.\n"
                "The chrome SINK has an empty medicine cabinent above it.\n"
                "The walk-in SHOWER has a detachable showerhead and multiple water pressure settings.\n"
                "The Passageway to the South is the only way out of here."
            )

        case "Passageway":
            print("The passage connects rooms in all directions. The wooden DOOR to the South seems different from the rest.")

        case "Gallery":
            print(
                "You stare in awe at the wonderous works of art on display here.\n"
                "A giant STATUE of some sort of bird draws your attention.\n"
                "You also notice a vibrant PAINTING framed beautifully on the wall.\n"
                "There are rooms to the North and West, as well as a METALDOOR leading to a room in the East."
            )

        case "Foyer":
            print(
                "You're almost free! You can see the front door to the East!\n"
                "Although, the Lounge back to the West is still tempting..."
            )
            if "Guard" in room.items:
                print("An intimidating looking GUARD blocks the exit. Is there a way around them?")
            if "Stick" in room.items:
                print("A long wooden STICK lies in the corner.")

        case "Study":
            print(
                "The dim lighting in the room sets the perfect mood.\n"
                "There are four BOOKS on the desk."
            )
            if "Candle" in room.items:
                print("A CANDLE with enough wax to last one full game is on the table.")
            print("The Living Room to the South is the only exit to the room.")

        case "Living Room":
            if room.prog == 0:
                print("The FIREPLACE's roaring flames warm up the room.")
            else:
                print("With the FIREPLACE out, the room feels much colder.")
            print(
                'A 70" TV is mounted to the wall.\n'
                'A single REMOTE sits on a side table near the FIREPLACE.'
                'There are rooms to the North and the West.'
            )

        case "Armory":
            print("The room is full of old weapons and armor that haven't seen much use recently.")
            if "Sword" in room.items:
                print("There's a brilliant steel SWORD on display.")
            print(
                "A well crafted SHIELD sits above the mantle in the back.\n"
                "An old suit of ARMOR rests on a stand in front of you.\n"
                "The West entrance is the only way in or out of the room"
            )
        
        case "Exit":
            print("The outdoors are lovely.")

        case _:
            # if player ends up in an inaccessible room
            print("How did you get here?")
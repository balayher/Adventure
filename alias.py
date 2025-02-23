def item_alias(item, room):
    # parses player's input to accept similar words
    match item:
        case "Rainslayer" | "Chef Rainslayer":
            item = "Chef"

        case "Chef's knife":
            item = "Knife"

        case "Red herring" | "Herring":
            item = "Fish"

        case "Giant table" | "Oak table":
            item = "Table"

        case "Opal vase":
            item = "Vase"

        case "Wooden bucket":
            item = "Bucket"

        case "Cans of food" | "Cans of broth" | "Broth cans" | "Food cans":
            item = "Cans"

        case "Bag of rice" | "Bags of rice" | "Bags" | "Bag":
            item = "Rice"
        
        case "Golden brain" | "Goldenbrain" | "Gold plated brain" | "Goldbrain" | "Gold brain" | "Gold-plated brain":
            item = "Brain"
        
        case "Door":
            if room.name == "Dungeon":
                item = "Celldoor"
            if room.name == "Gallery":
                item = "Metaldoor"

        case "Cell door":
            item = "Celldoor"

        case "Metal door":
            item = "Metaldoor"

        case "Goldcoin" | "Gold coin":
            item = "Coin"

        case "Silver clock":
            item = "Clock"

        case "Large sofa":
            item = "Sofa"

        case "Comfy chair":
            item = "Chair"

        case "Evan's diary" | "Worn diary" | "Old diary" | "Worn notebook" | "Notebook" | "Evan's notebook":
            item = "Diary"

        case "Wooden door" | "Wood door" | "Woodendoor" | "Wooddoor":
            if room.name == "Passageway":
                item = "Door"

        case "Bird statue" | "Giant statue" | "Parakeet statue" | "Conure statue" | "Golden conure statue":
            item = "Statue"

        case "Vibrant painting" | "Animal painting" | "Paintings":
            item = "Painting"

        case "Kujo" | "Guard Kujo":
            item = "Guard"

        case "Wooden stick" | "Long stick":
            item = "Stick"

        case "Bird book" | "Bird books" | "Book":
            item = "Books"
        
        case "Television":
            item = "Tv"

        case "Remote control" | "Television remote" | "Tv remote":
            item = "Remote"
        
        case "Fire" | "Fire place":
            item = "Fireplace"
        
        case "Small key":
            item = "Key"

        case "Key":
            if room.name == "Gallery":
                item = "Keyring"

        case "Ring of keys" | "Key ring":
            item = "Keyring"

        case "Steel sword":
            item = "Sword"

    return item
# Escape From Evan's Mansion

A text adventure game where you search for Evan's most prized possession and find a way to escape his mansion!

## Prerequisites

Before running this project locally, ensure you have the following installed:

- Python (version 3.1.0 or above)

## Available Actions

- Move (m): Move to another room.
- Look (l): Look around the current room for any interactable OBJECTS.
- Check (c): Check an OBJECT in the current room or your inventory. 
- Interact (i): Interact with an OBJECT. If it is collectable, add it to your inventory.
- Inventory (b): Check your current inventory.
- Use (u): Use an item from your inventory.
- Map: View a map of the rooms you have visited.
- Quit (q): Prompts to exit the game. Yes (y) confirms and exits the game.

When moving, you will be prompted for a direction to move in.
North (n), East (e), South (s), or West (w) will attempt to move you in the given direction.
Forwards (f), Backwards (b), Left (l), or Right (r) will attempt to move you in the given direction relative to your current facing (typically, this will be the direction you entered the room from).  
You may also move directly with just North (n), East (e), South (s), or West (w).  
Interacting with an item that's already in your inventory will attempt to Use the item instead.
Conversely, attempting to use an item that's not in your inventory but is in the current room will attempt to Interact with the item.  
Additional actions may be hidden as well. Experiment to find out!  


## Credits

Thanks to [boot.dev](https://www.boot.dev/) for the inspiration to push myself to attempt my first solo project from scratch.  
Thanks to my brother Evan for adding to the lore of the game.
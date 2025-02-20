# Adventure

A text adventure game. 

## Prerequisites

Before running this project locally, ensure you have the following installed:

- Python (version 3.1.0 or above)

## Available Actions

- Move (m): Move to another room.
- Inspect (i): Inspect the room for any interactable OBJECTS.
- Check (c): Check an OBJECT that appears in the current room. If it is collectable, add it to your inventory.
- Inventory (b): Check your current inventory.
- Exit (e): Prompts if you want to exit the game. Yes (y) confirms and exits the game.

When moving, you will be prompted for a direction to move in.
North (n), East (e), South (s), or West (w) will attempt to move you in the given direction.
Forwards (f), Backwards (b), Left (l), or Right (r) will attempt to move you in the given direction relative to your current facing (typically, this will be the direction you entered the room from).
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
- Exit: Exit the game.

When moving, you will be prompted for a direction to move in.
North, East, South, or West will attempt to move you in the given direction.
Forwards, Backwards, Left, or Right will attempt to move you in the given direction relative to your current facing (typically, this will be the direction you entered the room from).
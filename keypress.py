from typing import List, Dict

# Define a function to extract pressed status information from an event
def get_pressed_status(event):
    # Initialize an empty dictionary to store the extracted information
    result = {}

    # Split the string representation of the event and extract relevant information
    for part in str(event).split():
        # Extract and handle 'state=' information
        if 'state=' in part:
            state_value = part.split('=')[1]
            state_value = state_value.rstrip('>')
            result["state"] = state_value.split('|') if '|' in state_value else state_value

        # Extract and handle 'keysym=' information
        if 'keysym=' in part:
            key_value = part.split('=')[1]
            key_value = key_value.rstrip('>')
            result["key"] = key_value

    # Return the extracted information as a dictionary
    return result
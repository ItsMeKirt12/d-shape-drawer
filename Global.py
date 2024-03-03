class Global:

    # Initializing global variables with default values
    shape_name: str|None = None
    shape_class = None
    selected_shape = None

    # Static method to extract information about the pressed status from an event
    @staticmethod
    def get_pressed_status(event):
        # Initializing an empty dictionary to store the extracted information
        result = {}

        # Splitting the string representation of the event and extracting relevant information
        for part in str(event).split():
            # Extracting and handling the 'state=' information
            if 'state=' in part:
                state_value = part.split('=')[1]
                state_value = state_value.rstrip('>')
                result["state"] = state_value.split('|') if '|' in state_value else state_value

            # Extracting and handling the 'keysym=' information
            if 'keysym=' in part:
                key_value = part.split('=')[1]
                key_value = key_value.rstrip('>')
                result["key"] = key_value

        # Returning the extracted information as a dictionary
        return result
from customtkinter import CTkButton, CTkFrame
from CTkColorPicker import AskColor
from Global import Global
from typing import Type

class ColorPickerToggle(CTkButton):
    # Constructor method to initialize the ColorPickerToggle object
    def __init__(self, parent: Type[CTkFrame], app, *args, **kwargs):

        # Calling the constructor of the parent class (CTkButton) with specified parameters
        super().__init__(parent, *args, **kwargs)
        
        # Configuring the appearance of the button
        self.configure(corner_radius=0, text='Pick a Color', width=25, height=25)

        # Storing the reference to the main application
        self.app = app

    # Callback method that is triggered when the button is clicked
    def _clicked(self, event) -> None:
        # Calling the _clicked method of the parent class (CTkButton)
        super()._clicked(event)

        # Creating an instance of the color picker dialog
        pick_color: AskColor = AskColor()

        # Getting the chosen color from the color picker dialog
        chosen_color = pick_color.get()

        # Configuring the button's foreground color with the chosen color
        if chosen_color is not None:
            self.configure(fg_color=chosen_color)
            
            # Updating the color of the selected shape (if any)
            if Global.selected_shape:
                Global.selected_shape.set_new_color_from_hex(chosen_color)

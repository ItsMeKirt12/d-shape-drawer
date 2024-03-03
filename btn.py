from customtkinter import CTkButton
from Global import Global

class ShapeButton(CTkButton):

    # Constructor method for initializing the ShapeButton object
    def __init__(self, parent, app, shape_name, shape_class, *args, **kwargs):
        # Calling the constructor of the parent class (CTkButton) with specified parameters
        super().__init__(parent, text=shape_name, *args, **kwargs)
        
        # Storing the parameters as attributes of the ShapeButton object
        self.shape_name = shape_name
        self.shape_class = shape_class
        self.app = app

    # Callback method that is triggered when the button is clicked
    def _clicked(self, event):
        # Setting global variables to store the selected shape name and class
        Global.shape_name = self.shape_name
        Global.shape_class = self.shape_class
        
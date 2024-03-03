from tkinter import Menu
from color_picker import ColorPickerToggle
from save import export_to_file, import_from_file
from customtkinter import CTkFrame, CTkButton
from shapes_drawer import Shape
from Global import Global 
from tkinter import Button,Label
from tkinter.font import Font
from canvas import Canvas

class ShapeNavigation(CTkFrame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.width = 100
        self.height = 100 
        self.dragging = False

        # Create a dictionary of shape names and their corresponding classes
        shapes = {subclass.__name__: subclass for subclass in Shape.__subclasses__()}

        # Configure the grid layout
        self.columnconfigure(0, weight=1)

        # Button to clear the canvas
        clear_button = CTkButton(self, text="Clear", width=10, command=self.clear_canvas, fg_color="black", text_color="white")
        clear_button.grid(row=0, column=0, padx=5, pady=(5, 0), sticky="nsew")
        
        # Button for shape menu
        shape_menu_button = CTkButton(self, text="Shapes", width=10, fg_color="black", text_color="white")
        shape_menu_button.grid(row=0, column=1, padx=5, pady=(5, 0), sticky="nsew")
        shape_menu_button.bind("<Button-1>", self.show_shape_menu)

        adjust_label = Label(self, text="Color and Size", fg="white", bg="black")
        adjust_label.grid(row=1, column=2, columnspan=3, pady=(0, 5), sticky="nsew")

        # Create expanding button
        expand_button = Button(self, text="+", width=5, command=self.expand_shape, bg="gray", padx=0, highlightthickness=2, borderwidth=2)
        expand_button.grid(row=0, column=2, padx=0, sticky="nsew")  
        expand_button_font = Font(size=14)  
        expand_button['font'] = expand_button_font
        # Button to pick color using a color picker
        color = ColorPickerToggle(self, self.parent, text="Pick Color", width=15, text_color = "black")
        color.grid(row=0, column=3, padx=5, pady=(5, 0), sticky="nsew")  

        # Create shrinking button
        shrink_button = Button(self, text="-",width=5, command=self.shrink_shape, bg="gray", padx=0, highlightthickness=2, borderwidth=2)
        shrink_button.grid(row=0, column=4, padx=0, sticky="nsew")  
        shrink_button_font = Font(size=14)  # Adjust the size as needed
        shrink_button['font'] = shrink_button_font
        # Button to save the Shaped
        Save = CTkButton(self, text="Save", width=10, command=export_to_file, fg_color="black", text_color="white")
        Save.grid(row=0, column=5, padx=5, pady=(5, 0), sticky="nsew")  

        # Button to open a saved Shaped
        Open = CTkButton(self, text="Open", width=10, command=import_from_file,  fg_color="black", text_color="white")
        Open.grid(row=0, column=6, padx=5, pady=(5, 0), sticky="nsew")       
        
        # Create a Menu for shapes
        self.shape_menu = Menu(self, tearoff=0)
        for i, (shape_name, shape_class) in enumerate(shapes.items(), start=1):
            # Add each shape as a command in the menu
            self.shape_menu.add_command(label=shape_name, command=lambda s=shape_class: self.set_shape(s))

        # Center the buttons at the bottom
        for i in range(7):  # Adjust the range if you add more buttons
            self.columnconfigure(i, weight=1)
            self.rowconfigure(0, weight=1)

    # Display the shape menu
    def show_shape_menu(self, event):
        self.shape_menu.post(event.x_root, event.y_root)

    # Set the selected shape
    def set_shape(self, shape_class):
        Global.shape_name = shape_class.__name__
        Global.shape_class = shape_class
        self.parent.configure()

    # Function for the clear button
    def clear_canvas(self):
        Canvas.shapes = []  
        Canvas.redraw(self)  
        
    # Function for the expand button
    def expand_shape(self):
        if hasattr(self.parent, 'canvas'):
            self.parent.canvas.expand_shape()

    # Function for the shrink button
    def shrink_shape(self):
        if hasattr(self.parent, 'canvas'):
            self.parent.canvas.shrink_shape()

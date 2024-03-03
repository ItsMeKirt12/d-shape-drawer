from customtkinter import CTk
from canvas import Canvas
from nav import ShapeNavigation
from Global import Global

class MainApp(CTk):
    # Initialize the Application
    def __init__(self) -> None:
        super().__init__()

        # Define window dimensions
        window_height: int = 720
        window_width: int = 1280

        # Center the window on the screen
        screen_height: int = self.winfo_screenheight()
        screen_width: int = self.winfo_screenwidth()
        x_position: int|float = (screen_width - window_width) // 2
        y_position: int|float = (screen_height - window_height) // 2

        # Configure window geometry and title
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.title("2D Shape")

        # Create navigation bar
        shape_navigation = ShapeNavigation(self)
        shape_navigation.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Create drawing canvas
        self.canvas = Canvas(self)
        self.canvas.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Configure grid weights
        self.grid_rowconfigure(0, weight=1)     
        self.grid_columnconfigure(0, weight=0, uniform="nav_col")
        self.grid_columnconfigure(1, weight=1, uniform="nav_col")

        # Bind key press event
        self.bind("<Key>", self.key_press)

    def key_press(self, event) -> None:
        # Delegate key press handling to the drawing canvas
        
        self.canvas.key_pressed(event)
        # Rotate the selected shape based on key presses
        if event.char == "r" and Global.selected_shape:
            Global.selected_shape.rotate_right()
        elif event.char == "l" and Global.selected_shape:
            Global.selected_shape.rotate_left()

if __name__ == '__main__':
    MainApp().mainloop()

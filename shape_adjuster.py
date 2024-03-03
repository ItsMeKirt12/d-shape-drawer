from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from tkinter import Canvas

# Creating a ShapeAdjuster class that inherits from tkinter Canvas
class ShapeAdjuster(Canvas):

    # Constructor method to initialize the ShapeAdjuster object
    def __init__(self, start_x: int, start_y: int, end_x: int, end_y: int) -> None:
        # Calling the constructor of the parent class (Canvas)
        super().__init__()

        # Storing the coordinates and adjustment value as attributes
        self.start_x: int = start_x
        self.start_y: int = start_y
        self.end_x: int = end_x
        self.end_y: int = end_y
        self.adjust_value: int = 5

    # Method to draw the shape on the canvas
    def draw(self) -> None:
        # Setting color and line width
        glColor3f(0.5, 0.5, 0.5)
        glLineWidth(2)

        # Drawing a line between the specified coordinates
        glBegin(GL_LINES)
        glVertex2f(self.start_x, self.start_y)
        glVertex2f(self.end_x, self.end_y)
        glEnd()

    # Method to check if a given point is within the bounds of the shape
    def within_bounds(self, mouse_x: int, mouse_y: int) -> bool:
        return (
            min(self.start_x, self.end_x) <= mouse_x <= max(self.start_x, self.end_x) and
            min(self.start_y, self.end_y) <= mouse_y <= max(self.start_y, self.end_y)
        )
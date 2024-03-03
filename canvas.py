from pyopengltk import OpenGLFrame
from OpenGL.GLU import *
from OpenGL.GL import *
from keypress import get_pressed_status
from Global import Global
from rotate import rotate_shape 
import tkinter as tk
from shapes_drawer import Shape

class Canvas(OpenGLFrame):
    
    # Class-level variable to store a list of shapes
    shapes = []

    # Constructor method to initialize the Canvas object
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        tk.Frame.__init__(self, parent)
        OpenGLFrame.__init__(self, parent, **kwargs)

        # Binding methods to mouse and keyboard events
        self.bind("<Motion>", self._on_mouse_move)
        self.bind("<ButtonPress-1>", self._on_mouse_press)
        self.bind("<ButtonRelease-1>", self._on_mouse_release)
        self.bind("<Key>", self.key_pressed)

        # Storing the parent widget and initializing flags
        self.parent = parent
        self.dragging = False

    # Method to initialize OpenGL settings
    def initgl(self) -> None:
        glViewport(0, 0, self.width, self.height)
        glClearColor(0.17, 0.17, 0.17, 1.0)
        self.animate = 1
        self.dragging = False
        self.start_coordinates = None
        self.current_coordinates = None
        self.end_coordinates = None

    # Methods to manipulate the size of the selected shape
    def expand_shape(self):
        if Global.selected_shape:
            if isinstance(Global.selected_shape, Shape):
                Global.selected_shape.expand()

    def shrink_shape(self):
        if Global.selected_shape:
            if isinstance(Global.selected_shape, Shape):
                Global.selected_shape.shrink()

    # Method to handle keyboard input
    def key_pressed(self, event=None):
        if event:
            pressed_status = get_pressed_status(event)
            key = event.keysym

            if not Global.selected_shape:
                print("Please select a shape first!")
                return
        if hasattr(pressed_status, '__iter__'):
            state = pressed_status.get('state', None)

            # Handling movement and rotation of shapes
            if key == 'Up':
                Global.selected_shape.move_up()
            elif key == 'Down':
                Global.selected_shape.move_down()
            elif key == 'Left':
                Global.selected_shape.move_left()
            elif key == 'Right':
                Global.selected_shape.move_right()
            elif key == 'r':
                rotate_shape(Global.selected_shape, 10.0)
            elif key == 'l':
                rotate_shape(Global.selected_shape, -10.0)
            elif 'Control' in state and key in {'+', 'plus', '='}:
                self.expand_shape()
            elif 'Control' in state and key == '-':
                self.shrink_shape()

    # Method to handle mouse press events
    def _on_mouse_press(self, event):
        self.dragging = True
        self.start_coordinates = (event.x, event.y)
        self.current_coordinates = self.start_coordinates

        # Selecting a shape based on the mouse press event
        if not self.dragging == None and len(Canvas.shapes) > 0:
            for shape in Canvas.shapes[::-1]:
                if shape.within_bounds(event.x, event.y):
                    shape.selected = True
                    Global.selected_shape = shape
                    break
                else:
                    Global.selected_shape = None

            for shape in Canvas.shapes:
                if shape and shape != Global.selected_shape:
                    shape.selected = False

    # Method to handle mouse move events
    def _on_mouse_move(self, event):
        self.current_coordinates = (event.x, event.y)

    # Method to handle mouse release events
    def _on_mouse_release(self, event):
        self.dragging = False
        self.end_coordinates = self.current_coordinates
        self.current_coordinates = None

        # Creating a new shape based on the mouse release event
        if Global.shape_class:
            Canvas.shapes.append(
                Global.shape_class(self.start_coordinates, self.end_coordinates)
            )

            Global.shape_name = None
            Global.shape_class = None
            self.parent.configure(cursor="arrow")

    # Method to redraw the OpenGL canvas
    def redraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self.width, self.height, 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glClearColor(0.0, 0.0, 0.0, 0.0)

        # Drawing existing shapes on the canvas
        if len(Canvas.shapes) > 0:
            for shape in Canvas.shapes:
                shape.draw()

        # Drawing a line if dragging
        if self.dragging:
            glBegin(GL_LINES)
            glVertex2f(*self.start_coordinates)
            glVertex2f(*self.current_coordinates)
            glEnd()
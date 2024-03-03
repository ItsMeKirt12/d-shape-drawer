from typing import List, Tuple
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

class Shape():

    # Constructor to initialize shape attributes
    def __init__(
        self,
        number_of_sides: int,
        start_x_y: List[int],
        end_x_y: List[int]
    ) -> None:
        self.number_of_sides: int = number_of_sides
        self.start_x_y: List[int] = start_x_y
        self.end_x_y: List[int] = end_x_y
        self.angle = 2
        self.selected = False

        # Calculating center, half-size, and background color
        self.center_x: int|float = (self.start_x_y[0] + self.end_x_y[0]) / 2
        self.center_y: int|float = (self.start_x_y[1] + self.end_x_y[1]) / 2
        self.half_size: int|float = min(self.width, self.height) / 2
        self.background_color: Tuple[float, float, float] = (1.0, 1.0, 1.0)

    # Property methods to get width and height
    @property
    def width(self) -> int:
        return abs(self.start_x_y[0] - self.end_x_y[0])

    @property
    def height(self) -> int:
        return abs(self.start_x_y[1] - self.end_x_y[1])

    # Method to draw the shape
    def draw(self) -> None:
        if self.selected:
            glColor3f(*self.background_color)
        else:
            glColor3f(*self.background_color)

        glBegin(GL_POLYGON)
        for index in range(self.number_of_sides):
            angle = 2 * pi * index / self.number_of_sides + radians(self.angle)

            x: int | float = self.center_x + self.half_size * cos(angle)
            y: int | float = self.center_y + self.half_size * sin(angle)
            glVertex2f(x, y)
        glEnd()
    
    # Method to rotate the shape
    def rotate(self, angle_increment: float) -> None:
        self.angle += angle_increment

        # Update position based on the new angle
        self.center_x = (self.start_x_y[0] + self.end_x_y[0]) / 2
        self.center_y = (self.start_x_y[1] + self.end_x_y[1]) / 2

    # Methods to rotate shape left and right
    def rotate_left(self):
        self.rotate(-10.0) 

    def rotate_right(self):
        self.rotate(10.0)

    # Method to check if a point is within the shape bounds
    def within_bounds(self, mouse_x: int, mouse_y: int) -> bool:
        vertices = []

        for index in range(self.number_of_sides):
            angle = 2 * pi * index / self.number_of_sides + radians(self.angle)
            x = self.center_x + self.half_size * cos(angle)
            y = self.center_y + self.half_size * sin(angle)
            endpoint = (x, y)
            vertices.append(endpoint)

        crossings: int = 0

        for index in range(self.number_of_sides):
            start_x, start_y = vertices[index]
            end_x, end_y = vertices[(index + 1) % self.number_of_sides]

            if (start_y > mouse_y) != (end_y > mouse_y):
                if mouse_x < (end_x - start_x) * (mouse_y - start_y) / (end_y - start_y) + start_x:
                    crossings += 1

        return crossings % 2 == 1

    # Method to set new shape color from hex
    def set_new_color_from_hex(self, hex_color: str) -> None:
        hex_color = hex_color.lstrip('#')
        rgb: Tuple[int] = tuple(int(hex_color[index: index + 2], 16) / 255.0 for index in (0, 2, 4))
        self.background_color = rgb

    # Private method to change shape size
    def __change_shape(self, increment: bool=True) -> None:
        end_x = self.end_x_y[0]
        end_y = self.end_x_y[1]

        new_end_x = end_x + (10 if increment else -10)
        new_end_y = end_y + (10 if increment else -10)

        self.end_x_y = (new_end_x, new_end_y)

        new_width = abs(new_end_x - self.start_x_y[1])
        new_height = abs(new_end_y - self.start_x_y[1])

        self.half_size = max(new_width, new_height) / 2

    # Methods to expand and shrink the shape
    def expand(self) -> None:
        self.__change_shape(increment=True)

    def shrink(self) -> None:
        self.__change_shape(increment=False)


# Subclass for Triangle shape
class Triangle(Shape):

    def __init__(self, start_coordinates, end_coordinates):
        super().__init__(3, start_coordinates, end_coordinates)
        self.angle = 0
    
    # Methods to move the Triangle
    def move_right(self):
        self.center_x += 5

    def move_left(self):
        self.center_x -= 5

    def move_up(self):
        self.center_y -= 5

    def move_down(self):
        self.center_y += 5


# Subclass for Diamond shape
class Diamond(Shape):

    def __init__(self, start_coordinates, end_coordinates):
        super().__init__(4, start_coordinates, end_coordinates)
        self.angle = 0

    # Methods to move the Diamond
    def move_right(self):
        self.center_x += 5

    def move_left(self):
        self.center_x -= 5

    def move_up(self):
        self.center_y -= 5

    def move_down(self):
        self.center_y += 5


# Subclass for Octagon shape
class Octagon(Shape):

    def __init__(self, start_coordinates, end_coordinates):
        super().__init__(8, start_coordinates, end_coordinates)
        self.angle = 0

    # Methods to move the Octagon
    def move_right(self):
        self.center_x += 5

    def move_left(self):
        self.center_x -= 5

    def move_up(self):
        self.center_y -= 5

    def move_down(self):
        self.center_y += 5


# Subclass for Circle shape
class Circle(Shape):

    def __init__(self, start_coordinates, end_coordinates):
        super().__init__(100, start_coordinates, end_coordinates)
        self.angle = 0
        
    # Methods to move the Circle
    def move_right(self):
        self.center_x += 5

    def move_left(self):
        self.center_x -= 5

    def move_up(self):
        self.center_y -= 5

    def move_down(self):
        self.center_y += 5


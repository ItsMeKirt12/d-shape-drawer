from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from Global import Global

# this is the function for the rotation of the shapes.
def rotate_shape(shape, angle):
    if Global.selected_shape:
        Global.selected_shape.rotate(angle)
from PIL import Image
import numpy as np
class Canvas:
    """Object where all shapes are going to be drawn"""
    def __init__(self, height, width, color):
        self.color = color
        self.height = height
        self.width = width

        # Create a 3D numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change [0,0,0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


class Rectangle:
    """A rectangle shape that can be drawn on a Canvas object"""
    def __init__(self, x, y, height, width, color):

        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        """Draw itself into the canvas"""

        # Changes a slice of the array with new values
        canvas.data[self.x: self.x + self.height, self.y : self.y + self.width] = self.color
class Square:

    def __init__(self, x, y, side, color):
        self.color = color
        self.x = x
        self.y = y
        self.side = side

    def draw(self, canvas):
        """Draw itself into the canvas"""

        # Changes a slice of the array with new values
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


canvas = Canvas(height=20, width=30, color=(255,255,255))
r1 = Rectangle(x=1, y=6, height=7, width=10, color=(100,100,125))
r1.draw(canvas)
s1 = Square(x=1, y=3, side = 3, color=(0,100,222))
s1.draw(canvas)
canvas.make('canvas.png')

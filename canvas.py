#! python
import numpy as np
from PIL import Image

class Canvas:
    """
    Object where all shapes are going to be drawn.
    """
    def __init__(self, width, height, color):

        self.width = width
        self.height = height
        self.color = color

        # Create a 3d numpy area of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Updating color with user given values for color
        self.data[:] = self.color
    
    def make(self, imagepath):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)

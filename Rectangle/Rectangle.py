# Rectangle.py

class Rectangle(object):
    # Declare public methods here
    def __init__(self, length, width):
        # Set class instance variables here
        self.length = length
        self.width = width

    def calculateArea(self):
        # Write calculateArea here
        return self.length * self.width

    def calculatePerimeter(self):
        # Write calculatePerimeter here
        return 2* self.length + 2* self.width

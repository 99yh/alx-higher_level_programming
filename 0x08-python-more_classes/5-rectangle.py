#!/usr/bin/python3
"""Module for making and manipulating rectangles."""


class Rectangle:
    """Make a rectangle with Rectangle(<width>, <height>)"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle instence."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Get the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Get the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Represent the shape of the object."""
        if self.width == 0 or self.height == 0:
            return ""
        row = '#' * self.width + '\n'
        tot = row * self.height
        return tot[:-1]

    def __repr__(self):
        """Represent the object formally."""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Say farewell before you die"""
        print('Bye rectangle...')

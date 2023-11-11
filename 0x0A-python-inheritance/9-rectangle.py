#!/usr/bin/python3
"""Module to make and manipulate rectangles."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Make a rectangle object."""

    def __init__(self, width, height):
        """Usage: Rectangle(width, height) to make a new rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Get the area of the rectangle object."""
        return self.__width * self.__height

    def __str__(self):
        """Represent the rectangle in a human-readable form."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

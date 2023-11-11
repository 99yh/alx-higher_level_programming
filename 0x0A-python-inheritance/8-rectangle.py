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

#!/usr/bin/python3
"""Module to make and manipulate squares."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Make a square object."""

    def __init__(self, size):
        """Usage: Square(size) to make a new square."""
        self.integer_validator("size", size)
        super().__init__(size, size)

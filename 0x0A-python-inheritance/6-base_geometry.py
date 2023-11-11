#!/usr/bin/python3
"""Module to make and manipulate geometry."""


class BaseGeometry:
    """The base class of the geometry."""

    def area(self):
        """Calcutale the area of the geometry."""
        raise Exception("area() is not implemented")

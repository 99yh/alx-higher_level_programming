#!/usr/bin/python3
"""Make a circle using a MagicClass."""
import math


class MagicClass:
    """
    Make a circle.

    Parameters
    ----------
    radius : int or float
        default is 0

    Examples
    --------
    >>> my_circle = MagicClass()
    >>> my_circle = MagicClass(4.5)

    This will not work
    >>> my_circle = MagicClass("idk")
    Traceback (most recent call last):
        ...
    TypeError: radius must be a number
    """

    def __init__(self, radius=0):
        """Construct a  circle."""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of a circle.

        Examples
        --------
        >>> my_circle = MagicClass(4.5)
        >>> print('{:.2f}'.format(my_circle.area()))
        63.62
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the perimeter of a circle.

        Examples
        --------
        >>> my_circle = MagicClass(4.5)
        >>> print('{:.2f}'.format(my_circle.circumference()))
        28.27
        """
        return 2 * math.pi * self.__radius

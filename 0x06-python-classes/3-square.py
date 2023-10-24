#!/usr/bin/python3
"""Make a Square object."""


class Square:
    """
    Make a square.

    Examples
    --------
    >>> my_square = Square(3)
    >>> print(my_square.__dict__)
    {'_Square__size': 3}
    """
    def __init__(self, size=0):
        """
        Intialize a new instance.

        Arguments
        ---------
        size : int
            The size of the square

        Examples
        --------
        >>> my_square = Square(3)
        >>> print(my_square.size)
        Traceback (most recent call last):
            ...
        AttributeError: 'Square' object has no attribute 'size'
        >>> print(my_square.__size)
        Traceback (most recent call last):
            ...
        AttributeError: 'Square' object has no attribute '__size'

        Examples
        --------
        >>> my_square = Square("3")
        Traceback (most recent call last):
            ...
        TypeError: size must be an integer
        >>> my_square = Square(-3)
        Traceback (most recent call last):
            ...
        ValueError: size must be >= 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of a square.

        Examples
        --------
        >>> my_square = Square(5)
        >>> print(my_square.area())
        25
        """
        return self.__size ** 2

#!/usr/bin/python3
"""Make a Square object."""


class Square:
    """
    Make a square.

    Examples
    --------
    >>> my_square = Square(3)
    >>> print(type(my_square))
    <class '1-square.Square'>
    >>> print(my_square.__dict__)
    {'_Square__size': 3}
    """
    def __init__(self, size):
        """
        Intialize a new instance.

        Arguments
        ---------
        size:
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
        """
        self.__size = size

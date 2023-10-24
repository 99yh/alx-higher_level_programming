#!/usr/bin/python3
"""Make a Square object."""


class Square:
    """
    Make a square.

    Examples
    --------
    >>> my_square = Square(3)
    >>> print(type(my_square))
    <class '2-square.Square'>
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

#    @property
#    def __size(self):
#        self.__size = 0
#    @__size.setter
#    def __size(self, size):
#        """
#        Verify the field attribute __size.
#
#        This property handles wrong inputs for a square size
#        such as giving a NaN value or a negative number
#
#        Parameters
#        ----------
#        size : int
#            The size of the square
#
#        Examples
#        --------
#        >>> my_square = Square("3")
#            ...
#        TypeError: size must be an integer
#        >>> my_square = Square(-3)
#            ...
#        ValueError: size must be >= 0
#        """
#        if type(size) is not int:
#            raise TypeError("size must be an integer")
#        if size < 0:
#            raise ValueError("size must be >= 0")

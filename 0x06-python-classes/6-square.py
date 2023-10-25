#!/usr/bin/python3
"""Make a Square object."""


class Square:
    """
    Make a square.

    Arguments
    ---------
    size : int
        The size of the square
    position : tuple of two integers
        The coordinates of the square

    Examples
    --------
    >>> my_square = Square()
    >>> my_square = Square(3, (2, 1))
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Intialize a new instance.

        Arguments
        ---------
        size : int
        position : tuple of two integers

        Examples
        --------
        >>> my_square = Square(3, (2, 1))
        >>> print(my_square.__dict__)
        {'_Square__size': 3, '_Square__position': (2, 1)}
        
        adding size or position is optional
        >>> my_square = Square()
        >>> print(my_square.__dict__)
        {'_Square__size': 0, '_Square__position': (0, 0)}
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Examples
        --------
        >>> my_square = Square(89)
        >>> print(my_square.size)
        89
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square to a given value.

        Examples
        --------
        >>> my_square = Square()
        >>> my_square.size(3)
        >>> my_square.size("3")
        Traceback (most recent call last):
            ...
        TypeError: size must be an integer
        >>> my_square.size = -3
        Traceback (most recent call last):
            ...
        ValueError: size must be >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square

        Examples
        --------
        >>> my_square = Square()
        >>> print(my_square.position)
        (0, 0)
        >>> my_square.position = (3, 1)
        >>> print(my_square.position)
        (3, 1)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square

        Examples
        --------
        >>> my_square = Square(3, (2, 7))
        >>> my_square.position = (3, 1)
        >>> my_square.position = (0, 2)
        >>> my_square.position = "top"
        Traceback (most recent call last):
            ...
        TypeError: position must be a tuple of 2 positive integers
        >>> my_square.position = (None, 1)
        Traceback (most recent call last):
            ...
        TypeError: position must be a tuple of 2 positive integers
        """
        if (type(value) != tuple or len(value) != 2 or
            type(value[0]) != type(value[1]) != int or
            value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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

    def my_print(self):
        """
        Print out the square object.

        Examples
        --------
        >>> my_square = Square(2)
        >>> my_square.my_print()
        ##
        ##
        >>> my_square.size = 0
        >>> my_square.my_print()
        <BLANKLINE>
        >>> my_square.size = 3
        >>> my_square.position = (2, 1)
        >>> my_square.my_print()
        <BLANKLINE>
          ###
          ###
          ###
        """
        if self.__size == 0:
            print()
            return None
        line = ' ' * self.__position[0] + '#' * self.__size + '\n'
        print('\n' * self.__position[1] + line * self.__size, end='')

#!/usr/bin/python3
"""
The hardest way to add two numbers.

You can simply use the ``+`` operator but we provided
this module to illustrate tests and docstrings.
"""


def add_integer(a, b=98):
    """
    Add two numbers or one with 98

    Parameter
    ---------
    a: int or float
        first number
    b: int or float (default: 98)
        second number
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

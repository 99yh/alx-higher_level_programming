#!/usr/bin/python3
"""A well documented Hello World-level Module"""


def say_my_name(first_name, last_name=""):
    """
    Say "My name is <first_name> <last_name>"

    Args
    ----
    first_name : str
    last_name  : str, optional
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

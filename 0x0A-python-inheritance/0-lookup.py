#!/usr/bin/python3
"""Module to get informations about any object attributes."""


def lookup(obj):
    """Get a list of all attributes of an object."""
    return dir(obj)

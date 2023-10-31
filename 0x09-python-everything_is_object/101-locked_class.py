#!/usr/bin/python3
"""Module for making locked class."""


class LockedClass:
    """Only first name allowed as an attribute."""
    __slots__ = ('first_name',)

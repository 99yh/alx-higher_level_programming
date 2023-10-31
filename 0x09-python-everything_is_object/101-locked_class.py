#!/usr/bin/python3
class LockedClass:
    """Only first name allowed as an attribute."""
    __slots__ = ('first_name',)

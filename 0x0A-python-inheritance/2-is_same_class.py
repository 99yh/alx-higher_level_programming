#!/usr/bin/python3
"""Module to figure out who is who."""


def is_same_class(obj, a_class):
    """Check if `obj` is an instence of `a_class`."""
    return type(obj) is a_class

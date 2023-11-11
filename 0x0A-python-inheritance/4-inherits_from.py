#!/usr/bin/python3
"""Module to figure out is it inherited form it or not."""


def inherits_from(obj, a_class):
    """Check if `obj` is inherited directly or indirectly from `a_class`."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class

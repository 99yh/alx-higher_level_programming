#!/usr/bin/python3
"""Module to figure out is it kind or not."""


def is_kind_of_class(obj, a_class):
    """Check if `obj` is an instence of `a_class` or its superclasses."""
    return isinstance(obj, a_class)

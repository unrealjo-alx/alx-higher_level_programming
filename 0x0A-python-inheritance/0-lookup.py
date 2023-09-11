#!/usr/bin/python3
"""
lookup.py - A module providing the lookup() function.
"""


def lookup(obj):
    """a function that returns the list of available attributes
    and methods of an object.

    Args:
        obj (object): any object type

    Returns:
        list: A list object
    """

    return dir(obj)

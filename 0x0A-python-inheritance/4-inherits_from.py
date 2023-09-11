#!/usr/bin/python3
"""
4-inherits_from.py: A module providing the inherits_from() function
"""


def inherits_from(obj, a_class):
    """
    Check if object is an instance of specified class or its descendant.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if object is an instance of specified class or its descendant;
                otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

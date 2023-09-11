#!/usr/bin/python3
"""
3-is_kind_of_class.py: A module providing the is_kind_of_class() function
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or inherited from,
    the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of,
        or inherited from, the specified class; otherwise False.
    """
    return isinstance(obj, a_class)

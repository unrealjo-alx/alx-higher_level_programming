#!/usr/bin/python3
"""
8-class_to_json: A module providing the class_to_json() function.
"""


def class_to_json(obj):
    """A JSON serialization function returning
    a dictionary with simple data types.

    Args:
        obj (object): An instance of a Class

    Returns:
        dict: the dictionary description of obj.
    """
    return vars(obj)

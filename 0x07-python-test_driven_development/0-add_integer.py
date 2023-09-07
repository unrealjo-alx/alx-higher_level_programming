#!/usr/bin/python3
"""
0-add_integer.py : add_integer()
"""


def add_integer(a, b=98):
    """A function that adds 2 integers.

    Args:
        a (int,float): an integer/float
        b (int,float, optional): an integer/float. Defaults to 98.

    Raises:
        TypeError: If a or b are not an integers or float.

    Returns:
        int: The addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

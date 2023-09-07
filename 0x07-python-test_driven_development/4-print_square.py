#!/usr/bin/python3
"""
4-print_square.py : print_square()
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The length of the square to be printed.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

#!/usr/bin/python3

""" This module defines the Square class. """


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """
        Args:
            size (int, size): The size of the square. Defaults to 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

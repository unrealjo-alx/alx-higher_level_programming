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

    def area(self):
        """
        Computes the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size**2

    @property
    def size(self):
        """Retrieves the size of the square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

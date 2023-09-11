#!/usr/bin/python3
"""
10-square.py - A module providing the Square class.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Constructor for Square class."""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size**2

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"

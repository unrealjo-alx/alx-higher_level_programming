#!/usr/bin/python3
"""
square: A module providing the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square object."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square instance."""
        coordinates = f"{self._x}/{self._y}"
        return f"[Square] ({self.id}) {coordinates} - {self.width}"

#!/usr/bin/python3
"""
7-base_geometry.py - A module providing the BaseGeometry class.
"""


class BaseGeometry:
    """
    Base class for geometry-related classes.
    """

    def area(self):
        """
        Calculates the area.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

#!/usr/bin/python3
"""
base: A module providing the Base class to manage id attribute.
"""
import os

if not os.path.exists("models"):
    os.makedirs("models")
    with open("models/__init__.py", "w", encoding="utf-8"):
        pass


class Base:
    """
    Base class for managing id attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int, optional): The id value for the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

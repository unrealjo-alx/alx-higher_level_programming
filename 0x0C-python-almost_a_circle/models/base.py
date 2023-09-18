#!/usr/bin/python3
"""
base: A module providing the Base class to manage id attribute.
"""
import os
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            dicts_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(dicts_list)
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by the JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

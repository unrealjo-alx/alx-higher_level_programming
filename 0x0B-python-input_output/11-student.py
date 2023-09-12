#!/usr/bin/python3
"""
11-student: A module providing the Student class.
"""


class Student:
    """A class Student that defines a student."""

    def __init__(self, first_name, last_name, age):
        """The constructor

        Args:
            first_name (str): The first name.
            last_name (str): The last name.
            age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list, optional): A list of strings,. Defaults to None.

        Returns:
            dict:  a dictionary representation.
        """
        if not isinstance(attrs, list):
            return self.__dict__

        res = {}
        for attr in attrs:
            if self.__dict__.get(attr) is not None:
                res[attr] = self.__dict__.get(attr)
        return res

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        by values from json

        Args:
            json (dict): a dictionary of new values.
        """
        for key, value in json.items():
            if getattr(self, key) is not None:
                setattr(self, key, value)

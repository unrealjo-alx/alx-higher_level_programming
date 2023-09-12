#!/usr/bin/python3
"""
9-student: A module providing the Student class.
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        """
        return self.__dict__

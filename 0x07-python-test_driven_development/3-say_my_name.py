#!/usr/bin/python3
"""
	3-say_my_name.py: say_my_name()
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    full_name = first_name + " " + last_name if last_name else first_name
    print("My name is", full_name)

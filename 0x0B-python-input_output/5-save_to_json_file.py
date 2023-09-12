#!/usr/bin/python3
"""
5-save_to_json_file: A module providing the save_to_json_file() function.
"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj (object): an Object
        filename (str): the file name
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)

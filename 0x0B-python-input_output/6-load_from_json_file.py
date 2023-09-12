#!/usr/bin/python3
"""
6-load_from_json_file: A module providing the load_from_json_file() function.
"""
import json


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”:

    Args:
        filename (str): the file name.

    Returns:
        object: Deserialized python object.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

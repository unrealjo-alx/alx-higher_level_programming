#!/usr/bin/python3
"""
3-to_json_string: A module providing the to_json_string() function.
"""
import json


def to_json_string(my_obj):
    """
    A function that returns the JSON representation of an object (string).
    """
    return json.dumps(my_obj)

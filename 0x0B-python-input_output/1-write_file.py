#!/usr/bin/python3
"""
1-write_file: A module providing the write_file() function.
"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file.

    Args:
        filename (str, optional): the file name.
        Defaults to "".
        text (str, optional): text to be written into the file.
        Defaults to "".

    Returns:
        int: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

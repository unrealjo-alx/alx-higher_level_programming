#!/usr/bin/python3
"""
2-append_write.py: A module providing the append_write() function.
"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file.

    Args:
        filename (str, optional): the file name.
        Defaults to "".
        text (str, optional): text to be written into the file.
        Defaults to "".

    Returns:
        int: the number of characters written
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)

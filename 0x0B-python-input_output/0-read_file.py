#!/usr/bin/python3
"""
0-read_file: A module providing the read_file() function.
"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout:

    Args:
        filename (str, optional): The file name.
        Defaults to "".
    """
    with open(file=filename, mode="r", encoding="utf-8") as file:
        line = file.readline()
        while line:
            print(line, end="")
            line = file.readline()

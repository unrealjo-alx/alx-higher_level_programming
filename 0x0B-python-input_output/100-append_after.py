#!/usr/bin/python3
"""
100-append_after: A module providing the append_after() function.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text into a file after each line containing a specific string.

    Args:
        filename (str): The file name.
        search_string (str): The string to search for.
        new_string (str): The string to be inserted.
    """
    lines = []

    with open(filename, "r", encoding="utf-8") as r_file:
        lines = r_file.readlines()
        for line in lines:
            index = line.find(search_string)
            if index != -1:
                lines.insert(index, new_string)

    with open(filename, "w", encoding="utf-8") as w_file:
        w_file.writelines(lines)

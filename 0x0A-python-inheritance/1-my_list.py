#!/usr/bin/python3
"""
1-my_list.py - A module providing the MyList class.
"""


class MyList(list):
    """
    A custom list class that extends the built-in list class.
    """

    def __init__(self, *args):
        """Initialize the MyList object."""
        super().__init__(*args)

    def print_sorted(self):
        """Print a sorted version of the list."""
        array = sorted(self)
        print(array)

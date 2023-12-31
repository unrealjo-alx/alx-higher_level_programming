#!/usr/bin/python3


def safe_print_integer(value):
    """A function that prints an integer."""
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    return True

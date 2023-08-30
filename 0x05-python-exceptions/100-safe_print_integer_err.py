#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """A function that prints an integer."""
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        sys.stderr.write(f"Exception: {err}\n")
        return False
    return True

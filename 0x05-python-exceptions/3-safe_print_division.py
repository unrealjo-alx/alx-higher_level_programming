#!/usr/bin/python3


def safe_print_division(a, b):
    """A function that divides 2 integers and prints the result."""
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
        return None
    finally:
        print("Inside result: {}".format(result))
    return result

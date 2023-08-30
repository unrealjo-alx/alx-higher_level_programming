#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """A function that prints the first x elements of a list and only integers."""
    count = 0
    try:
        for idx in range(x):
            if isinstance(my_list[idx], int):
                print("{:d}".format(my_list[idx]), end="")
                count += 1
    except IndexError:
        pass
    finally:
        print("")
    return count

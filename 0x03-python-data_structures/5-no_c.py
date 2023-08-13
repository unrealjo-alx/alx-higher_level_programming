#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    arr = [char for char in my_string if char != "c" and char != "C"]
    return "".join(arr)

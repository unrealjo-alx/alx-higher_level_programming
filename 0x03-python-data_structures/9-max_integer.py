#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    max_n = my_list[0]
    for number in my_list:
        if number > max_n:
            max_n = number
    return max_n

#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or list.__len__ == 0:
        return 0
    sums = 0
    factor = 0
    for _set in my_list:
        sums += _set[0] * _set[1]
        factor += _set[1]
    # Avoid division by zero
    if factor == 0:
        factor = 1
    return sums / factor

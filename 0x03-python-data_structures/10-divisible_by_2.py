#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return []
    new_arr = my_list.copy()
    for i in range(len(my_list)):
        new_arr[i] = new_arr[i] % 2 == 0
    return new_arr

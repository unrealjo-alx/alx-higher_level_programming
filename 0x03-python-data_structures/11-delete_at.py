#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0 or len(my_list) < idx or idx < 0:
        return my_list
    my_list = [my_list[i] for i in range(len(my_list)) if i != idx]
    return my_list

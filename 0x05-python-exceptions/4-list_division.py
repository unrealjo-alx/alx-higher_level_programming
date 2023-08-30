#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """A function  that divides element by element 2 lists."""
    divisions = []
    for idx in range(list_length):
        result = 0
        try:
            result = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            divisions.append(result)
    return divisions

#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_integer = my_list[0]
    for i in my_list:
        if max_integer < i:
            max_integer = i
    return max_integer

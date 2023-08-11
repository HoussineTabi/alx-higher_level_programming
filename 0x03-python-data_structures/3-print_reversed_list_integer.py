#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print a list of integers in reversed order
       Arguments:
                 my_list: the list of integers
    """
    length = len(my_list)
    for i in range(length):
        print("{}".format(my_list[length - i - 1]))

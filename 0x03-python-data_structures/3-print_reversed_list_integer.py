#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print a list of integers in reversed order
       Arguments:
                 my_list: the list of integers
    """
    if my_list.isempty():
        return
    for i in reversed(my_list):
        print("{:d}".format(i))

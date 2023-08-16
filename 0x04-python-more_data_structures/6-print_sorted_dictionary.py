#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_of_keys = [x for x in a_dictionary]
    list_of_keys.sort()
    for key in list_of_keys:
        print("{}: {}".format(key, a_dictionary[key]))

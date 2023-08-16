#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict()
    list_keys = [key for key in a_dictionary]
    for i in list_keys:
        new_dict[i] = a_dictionary[i] * 2
    return new_dict

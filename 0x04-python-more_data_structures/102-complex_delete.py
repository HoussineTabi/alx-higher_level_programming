#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = [x for x in a_dictionary]
    for key in key_list:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return (a_dictionary)

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """this function is duplicat a list with the new modification
    Arguments:
              my_list: the list of integer
              idx: the index of the element to change
              elemnt: the new value of the element
    Return:
           return the new list after modification
    """
    new_list = []
    if len(my_list) < idx + 1 or idx < 0:
        new_list = list(my_list)
        return (new_list)
    new_list = list(my_list)
    new_list[idx] = element
    return (new_list)

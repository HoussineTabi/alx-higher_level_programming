#!/usr/bin/python3
def element_at(my_list, idx):
    """This function returns an element from a list at
       index if the item is exist and None otherwise
       Arguments:
                 my_list: the list of integers
                 idx: the index of elemnt
       Return: the element if exist and None otherwise
       """
    if len(my_list) < idx or idx < 0 or len(my_list) == 0:
        return (None)
    return (my_list[idx])

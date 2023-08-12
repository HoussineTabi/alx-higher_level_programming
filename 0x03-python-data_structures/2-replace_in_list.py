#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """This function modfied an element of a list with an
       an index gevn
       Arguments:
                 my_list: the list of integer
                 idx: the indx to change
                 element: the value of the new element
       Return: the list anyway
    """
    if len(my_list) < idx + 1 or idx < 0:
        return (my_list)
    my_list[idx] = element
    return (my_list)

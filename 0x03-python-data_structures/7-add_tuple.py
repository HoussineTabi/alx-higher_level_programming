#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """This function add to tuple together in a new tuple
       Return: the new tuple
    """
    sum_element = []
    a = max(len(tuple_a), len(tuple_b))
    if a < 2:
        a = 2
    for i in range(a):
        if i < len(tuple_a) and i < len(tuple_b):
            sum_element.append(tuple_a[i] + tuple_b[i])
        elif len(tuple_b) > i:
            sum_element.append(tuple_b[i])
        elif len(tuple_a) > i:
            sum_element.append(tuple_a[i])
        else:
            sum_element.append(0)
    return (sum_element[0], sum_element[1])

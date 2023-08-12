#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """This function add to tuple together in a new tuple
       Return: the new tuple
    """
    sum_element = []
    a = max(len(tuple_a), len(tuple_b))
    for i in range(a):
        if i < len(tuple_a) and i < len(tuple_b):
            sum_element.append(tuple_a[i] + tuple_b[i])
        elif len(tuple_a) <= i:
            sum_element.append(tuple_b[i])
        else:
            sum_element.append(tuple_a[i])
    sum_element = tuple(sum_element[0:2])
    return (sum_element)

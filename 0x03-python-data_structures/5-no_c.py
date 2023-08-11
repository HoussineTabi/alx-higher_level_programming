#!/usr/bin/python3
def no_c(my_string):
    """this function use to remove c and C from my string
        Arguments:
                  my_string: the string to change
        Return: the new string after modification
    """
    new_str = ''
    for i in range(len(my_string)):
        if my_string[i] in 'cC':
            continue
        new_str += my_string[i]
    return (new_str)

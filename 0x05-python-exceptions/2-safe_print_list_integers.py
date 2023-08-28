#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real_number_printed = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                real_number_printed += 1
        except TypeError:
            continue
    print()
    return (real_number_printed)

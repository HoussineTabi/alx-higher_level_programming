#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set(set_1)
    for i in set_2:
        if i in set_1:
            set_3.remove(i)
        else:
            set_3.add(i)
    return set_3

#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    best_key = [x for x in a_dictionary]
    x = best_key[0]
    for i in best_key:
        if a_dictionary[i] > a_dictionary[x]:
            x = i
    del i
    return x

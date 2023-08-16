#!/usr/bin/python3
def roman_to_int(roman_string):
    """This function converts a Roman
       number tu an integer number"""
    if type(roman_string) is not str or roman_string is None:
        return 0
    number = 0
    rm_dt = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    j = 0
    x = None
    for i in roman_string:
        if j == 0:
            x = i
            j = 1
        if rm_dt[i] > rm_dt[x]:
            number = (number + rm_dt[i] - 2 * rm_dt[x])
        else:
            number += rm_dt[i]
        x = i
    return number

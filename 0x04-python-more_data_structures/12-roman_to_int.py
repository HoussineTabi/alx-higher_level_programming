#!/usr/bin/python3
def roman_to_int(roman_string):
    """This function converts a Roman
       number tu an integer number"""
    if type(roman_string) is not str or len(roman_string) == 0:
        return 0
    number = 0
    roman_dict = {"I": 1, "II": 2, "III": 3, "IV": 4,
                  "V": 5, "VI": 6, "VII": 7, "VIII": 8,
                  "IX": 9, "X": 10, "L": 50, "C": 100,
                  "D": 500, "M": 1000}
    j = 0
    x = None
    for i in roman_string:
        if j == 0:
            x = i
            j = 1
        if roman_dict[i] < roman_dict[x]:
            number = (2 * number + roman_dict[i] - number)
        else:
            number += roman_dict[i]
        x = i
    return number

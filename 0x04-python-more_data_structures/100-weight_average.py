#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    average = 0
    devided = 0
    for (i, j) in my_list:
        average += i * j
        devided += j
    return (average / devided)

#!/usr/bin/python3
def print_last_digit(number):
    r = 0
    r = number % 10
    if number < 0:
        r = r - 10
    print("{}".format(r),sep='', end='')
    return (r)

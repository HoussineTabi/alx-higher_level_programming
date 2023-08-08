#!/usr/bin/python3
def print_last_digit(number):
    r = number % 10
    if number < 0:
        r = r - 10
    return (r)

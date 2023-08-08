#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz".format(), sep='', end=' ')
        elif i % 5 == 0:
            if i != 100:
                print("Buzz".format(), sep='', end=' ')
            else:
                print("Buzz".format())
        elif i % 3 == 0:
            print("Fizz".format, sep='', end=' ')
        else:
            print("{}".format(i), end='')


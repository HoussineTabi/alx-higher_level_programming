#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_dig = number % 10
if lst_dig > 5:
    print(f"Last digit of {number} is {lst_dig} and is greater than 5")
elif lst_dig < 5 and lst_dig != 0:
    print(f"Last digit of {number} is {lst_dig} and is less than 6 and not 0")
else:
    print("Last digit of {} is {} and is 0".format(number, lst_dig))

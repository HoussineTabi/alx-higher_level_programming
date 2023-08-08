#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ls = number % 10
str1 = "Last digit of "
if ls > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, ls))
elif ls < 5 and ls != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, ls))
else:
    print("{}{} is {} and is 0".format(str1, number, ls))

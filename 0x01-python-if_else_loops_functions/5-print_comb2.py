#!/usr/bin/python3
for _ in range(100):
    if _ != 99:
        print("{:02},".format(_), sep='', end=' ')
    else:
        print("{}".format(_))

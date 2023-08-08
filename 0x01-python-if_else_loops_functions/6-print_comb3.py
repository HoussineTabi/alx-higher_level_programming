#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i != j and i != 8:
            print("{}{},".format(i, j), sep='', end=' ')
        if i != j and i == 8:
            print("{}{}".format(i, j))

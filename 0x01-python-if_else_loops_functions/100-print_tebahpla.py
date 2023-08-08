#!/usr/bin/python3
str1 = ''
for i in range(122, 96, -1):
    if i % 2 != 0:
        str1 += chr(65 + i - ord("a"))
    else:
        str1 += chr(i)
print("{}".format(str1), end='')

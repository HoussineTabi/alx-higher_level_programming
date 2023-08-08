#!/usr/bin/python3
def uppercase(str):
    str1 = ''
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            str1 += chr(ord(i) % 97 + 65)
        else:
            str1 += i
    print(str1)

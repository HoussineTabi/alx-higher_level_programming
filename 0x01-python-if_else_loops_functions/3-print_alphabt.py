#!/usr/bin/python3
for i in range(len("abcdefghijklmnopqrstuvwxyz")):
    if "abcdefghijklmnopqrstuvwxyz"[i] == 'e':
        continue
    if "abcdefghijklmnopqrstuvwxyz"[i] == 'q':
        continue
    print(f'{"abcdefghijklmnopqrstuvwxyz"[i]}', sep='', end='')

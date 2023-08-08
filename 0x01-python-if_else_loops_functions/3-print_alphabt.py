#!/usr/bin/python3
for _ in range(len("abcdefghijklmnopqrstuvwxyz")):
    if "abcdefghijklmnopqrstuvwxyz"[_] == 'e':
        continue
    if "abcdefghijklmnopqrstuvwxyz"[_] == 'q':
        continue
    print(f'{"abcdefghijklmnopqrstuvwxyz"[_]}', sep='', end='')

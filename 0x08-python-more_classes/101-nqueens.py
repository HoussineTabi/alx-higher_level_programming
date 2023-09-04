#!/usr/bin/python3
"""
The queens Module
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(sys.argv[1])
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at less 4")
    else:
        for i in range(1, N - 1):
            lst = []
            num = 0
            for j in range(N):
                if j == 0:
                    num = i
                else:
                    num += 2
                if num >= N:
                    num = 0
                lst.append([j, num])
            print(lst)
except ValueError as e:
    print("N must be a number")

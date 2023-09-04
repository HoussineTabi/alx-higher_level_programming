#!/usr/bin/python3
"""
The queens Module
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
N = int(sys.argv[1])
if not isinstance(N, int):
    print("N must be a number")
else:
    if N < 4:
        print("N must be at less 4")
    else:
        for i in range(1, N - 1):
            lst = []
            for j in range(N):
                if i + 2 * j < N:
                    lst.append([j, i + 2 * j])
                else:
                    lst.append([j, abs(N - 2 * j)])
            print(lst)

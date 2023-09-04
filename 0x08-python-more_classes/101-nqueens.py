#!/usr/bin/python3
"""
The queens Module
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if not isinstance(sys.argv[1], int):
    print("N must be a number")
else:
    if sys.argv[1] < 4:
        print("N must be at less 4")

#!/usr/bin/python3
"""
Module of how to print a square use #
"""


def print_square(size):
    """
    The function that prints a square
    """
    if isinstance(size, int):
        if size >= 0:
            for i in range(size):
                print("#" * size)
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")

#!/usr/bin/python3
"""
Module to add to integers
"""


def add_integer(a, b=98):
    """
    add_integer: adds two integer and returns the result
    >>> add_integer(1, 2)
    3
    >>> add_integer(100,-2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(True, 1)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(-2, "a")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    """
    if a == None:
        return
    if type(a) in [int, float]:
        a = int(a)
        if type(b) in [int, float]:
            b = int(b)
            return a + b
        else:
            raise TypeError("b must be an integer")
    raise TypeError("a must be an integer")


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")

#!/usr/bin/python3
"""
Checks if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    checks if the objec in the class
    """
    return isinstance(obj, a_class)


if __name__ == "__main__":
    print(is_same_class(27441, int))

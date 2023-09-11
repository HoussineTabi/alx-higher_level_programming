#!/usr/bin/python3
"""
The module of the type of an object
"""


def is_kind_of_class(obj, a_class):
    """
    check if the object is a kind of class
    """

    return issubclass(obj.__class__, a_class)


if __name__ == "__main__":
    print(is_kind_of_class(3, int))
    print(is_kind_of_class(3, float))
    print(is_kind_of_class(3, object))

#!/usr/bin/python3
"""
check if an object is from a a class or a base class
"""


def inherits_from(obj, a_class):
    """
    lookup of the object in the class and the base class
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class

if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))

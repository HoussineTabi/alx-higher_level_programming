#!/usr/bin/python3
"""
lookup for the attributes and methods of an object
"""


def lookup(obj):
    """
    lookup for the attributes and methods of an object
    """
    return (dir(obj))


if __name__ == "__main__":
    lookup([True, False])

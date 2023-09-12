#!/usr/bin/python3
"""
This is the module documentation
"""


def class_to_json(obj):
    """
    unction that returns the dictionary
    data structure
    """
    att = obj.__dict__
    ser = {}
    for k, v in att.items():
        if isinstance(v, (list, dict, str, int, bool)):
            ser[k] = v
    return ser


if __name__ == "__main__":
    print()

#!/usr/bin/python3
"""
This is the module documentation
"""


def class_to_json(obj):
    """
    unction that returns the dictionary
    data structure
    """
    dict_attributes = vars(obj)
    return json.dumps(dict_attributes)


if __name__ = "__main__":
    print()

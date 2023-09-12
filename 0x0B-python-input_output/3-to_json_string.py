#!/usr/bin/python3
"""
Module to read json data type
"""
import json


def to_json_string(my_obj):
    """
    Return the json representation of an object
    """
    return json.dumps(my_obj)


if __name__ == "__main__":
    print()

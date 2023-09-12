#!/usr/bin/python3
"""
module use joison to string into data
"""
import json


def from_json_string(my_str):
    """
    convert string into data
    """
    return json.loads(my_str)


if __name__ == "__main__":
    print()

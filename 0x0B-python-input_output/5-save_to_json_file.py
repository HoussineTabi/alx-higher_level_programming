#!/usr/bin/python3
"""
Module to use json representaiton
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file writes an object to a file text using json
    """
    a = 0
    with open(filename, "w", encoding="utf-8") as f:
        a = f.writ(json.dump(my_obj))


if __name__ == "__main__":
    print()

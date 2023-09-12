#!/usr/bin/python3
"""
how to load from a file json
"""
import json

def load_from_json_file(filename):
    """
    load the data from a file json file
    """
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())


if __name__ == "__main__":
    print()

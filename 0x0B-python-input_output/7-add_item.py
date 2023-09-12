#!/usr/bin/python3
"""
the scrinpt to read and write from a json file
"""
import json
import sys

filename = "add_item.json"

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
arguments = sys.argv[1:]
save_to_json_file(arguments, filename)
load_from_json_file(filename)
if __name__ == "__main__":
    print()

#!/usr/bin/python3
"""
the scrinpt to read and write from a json file
"""
import json
import sys
from os import path

filename = "add_item.json"

if path.exists(filename):
    my_lst = __import__("6-load_from_json_file").load_from_json_file(filename)
else:
    my_lst = []

for arg in sys.argv[1:]:
    my_lst.append(arg)

__import__("5-save_to_json_file").save_to_json_file(my_lst, filename)
if __name__ == "__main__":
    print()

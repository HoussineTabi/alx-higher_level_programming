#!/usr/bin/python3
"""this place ofcomment that describes my models"""
import json
import sys
import os.path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
filename = "add_item.json"
my_list = []

if os.path.exists(filename) and os.path.getsize(filename) > 0:
    my_list = load_from_json_file(filename)

if len(sys.argv) > 1:
    for elem in sys.argv[1:]:
        my_list.append(elem)

save_to_json_file(my_list, filename)

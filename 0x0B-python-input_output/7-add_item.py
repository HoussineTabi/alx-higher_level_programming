#!/usr/bin/python3
"""
the scrinpt to read and write from a json file
"""
import json
import sys
from os import path



sv_to_j_fil = __import__("5-save_to_json_file").save_to_json_file
ld_fm_j_fil = __import__("6-load_from_json_file").load_from_json_file


if path.exists(filename):
    my_list = ld_fm_j_fil(filname)
else:
    my_list = []

for arg in sys.argc[1:]:
    my_list.append(arg)

sv_to_j_fil(my_list, filename)
if __name__ == "__main__":
    print()

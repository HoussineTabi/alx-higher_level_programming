#!/usr/bin/python3
def magic_string(iterator={"first":0}):
    iterator["first"] = iterator["first"] + 1
    return "BestSchool" + ", BestSchool" * (iterator["first"] - 1)

#!/usr/bin/python3
"""
Module of a function appending in file
"""


def append_write(filename="", text=""):
    """
    append_write used to appending in a file
    """
    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(filename, text)


if __name__ == "__main__":
    print()

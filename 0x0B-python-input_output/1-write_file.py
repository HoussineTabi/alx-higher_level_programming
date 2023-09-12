#!/usr/bin/python3
"""
Module to write into file with python
"""


def write_file(filename="", text=""):
    """
    write into a file
    """
    with open(filename, "w+", encoding="utf-8") as f:
        return f.write(text)


if __name__ == "__main__":
    print()

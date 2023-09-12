#!/usr/bin/python3
"""
Module of a function that read a file using the encoding utf8
"""


def read_file(filename=""):
    """
    read_file is a function that read a file
    Arguments:
              filename: the name of the file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    print(read_file("hello"))

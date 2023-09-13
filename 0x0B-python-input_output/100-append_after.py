#!/usr/bin/python3
"""
Mode of appending a line after each line in a file
"""


def append_after(filename='', search_string='', new_string=''):
    """
    discription of the function append_after
    """
    list_of_text = list()
    with open(filename, "r", encoding="utf-8") as f:
        list_of_text = f.read().split(search_string)
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(len(list_of_text)):
            f.write(list_of_text[i] + '\n')
            if i != len(list_of_text) - 1:
                f.write(new_string)


if __name__ == "__main__":
    print()
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

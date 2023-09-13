#!/usr/bin/python3
"""
Mode of appending a line after each line in a file
"""


def append_after(filename='', search_string='', new_string=''):
    """
    discription of the function append_after
    """
    file_text = ''
    with open(filename, "r", encoding="utf-8") as f:
        file_text = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in file_text:
            s = line
            if search_string in line:
                s += new_string
            f.write(s)



if __name__ == "__main__":
    print()
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

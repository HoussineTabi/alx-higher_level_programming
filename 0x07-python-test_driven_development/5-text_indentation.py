#!/usr/bin/python3
"""
Convert text to sentences
"""


def text_indentation(text):
    """
    text_indentation: converts a text into sentneces
    """
    if isinstance(text, str):
        check = 0
        for i in text:
            if i in ['.', '?', ':']:
                print(i, '\n', sep='')
                check = 0
            else:
                if i == ' ' and check == 0:
                    continue
                print(i, sep='', end='')
                check = 1
    else:
        raise TypeError("text must be a string")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
    text_indentation("Hello, World!")

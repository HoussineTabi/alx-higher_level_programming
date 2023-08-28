#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    strerr = "Exception: Unknown format code 'd' for object of type 'str'"
    strerr1 = "Except: "
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("{}".format(strerr), file=sys.stderr)
        return False

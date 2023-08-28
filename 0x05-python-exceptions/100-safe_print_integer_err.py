#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    re_v = False
    try:
        print("{:d}".format(value))
        re_v = True
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
    except TypeError as err:
        print("Exception: {}".fomat(err), file=sys.stderr)
    finally:
        return re_v

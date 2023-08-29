#!/usr/bin/python3
import sys


def safe_function(fct, *arg):
    a = None
    try:
        a = fct(*arg)
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
    except TypeError as err:
        print("Exception: {}".format(err), file=sys.stderr)
    except ZeroDivisionError as err:
        print("Exception: {}".format(err), file=sys.stderr)
    except IndexError as err:
        print("Exception: {}".format(err), file=sys.stderr)
    except NameError as err:
        print("Exception: {}".format(err), file=sys.stderr)
    finally:
        return a
def print_list(my_list, len):
    i = 0
    while i < len:
        print(my_list[i])
        i += 1
    return len

result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))

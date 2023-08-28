#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        if isinstance(a, int) and isinstance(b, int):
            result = a / b
    except (ZeroDivisionError, ValueError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result

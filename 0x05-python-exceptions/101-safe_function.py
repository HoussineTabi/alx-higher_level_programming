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

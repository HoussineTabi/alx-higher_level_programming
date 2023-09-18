#doctest_simple.py
import doctest
def my_function(a, b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function(2, 3)
    'aaa'
    """
    return a * b

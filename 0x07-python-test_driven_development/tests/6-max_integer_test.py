#!/usr/bin/python3
"""
Test a code using the unittest module
"""
import unittest
max_integer = __import__("max_integer").max_integer


class testMaxinteger(unittest.TestCase):
    """
    Class to test my code the max integer
    """

    def test_regular_max(self):
        """
        test the regular output
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
    print(Max_integer.max_integer([1, 3]))

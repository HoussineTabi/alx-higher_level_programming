#!/usr/bin/python3
"""
Test a code using the unittest module
"""
import unittest
import Max_integer


class testMaxinteger(unittest.TestCase):
    """
    Class to test my code the max integer
    """
    def test_regular_max(self):
        """
        test the regular output
        """
        self.assertEqual(Max_integer.max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(Max_integer.max_integer([]), None)
if __name__ == "__main__":
    unittest.main()
    print(Max_integer.max_integer([1, 3]))


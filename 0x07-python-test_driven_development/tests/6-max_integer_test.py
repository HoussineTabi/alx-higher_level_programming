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

    def test_docstr_module(self):
        """
        test the existance of the module doc
        """
        docstr = __import__("max_integer").__doc__
        self.assertTrue(len(docstr) > 1)

    def test_docstr_func(self):
        """
        checking for the docstr function
        """
        docstr = __import__("max_integer").max_integer.__doc__
        self.assertTrue(len(docstr) > 1)

    def test_empty(self):
        """
        checking for the empty list
        """
        self.assertIsNone(max_integer([]))

    def test_regular_max(self):
        """
        test the regular output
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)


if __name__ == "__main__":
    unittest.main()
    print(Max_integer.max_integer([1, 3]))

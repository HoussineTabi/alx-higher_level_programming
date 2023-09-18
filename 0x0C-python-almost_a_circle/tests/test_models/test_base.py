#!/usr/bin/python3
"""
The module test of the base with framework unittest
"""
import sys
import unittest
from models.base import Base


class testBase(unittest.TestCase):
    """
    the class test of the Base class
    """

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()

    def test_id(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.b3 = Base(12)
        self.assertEqual(self.b3.id, 12)
        self.b4 = Base()
        self.assertEqual(self.b4.id, 4)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""
The module test of the class Rectangle
"""
import sys
import unittest
from unittest.mock import patch
path = "/home/vagrant/alx/alx-higher_level_programming"
path += "/0x0C-python-almost_a_circle/models"
sys.path.append(path)
from rectangle import Rectangle
import io


class testRectangle(unittest.TestCase):
    """
    The class test of Rectangle
    """

    def test_id(self):
        """
        check the id of a rectangle
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_raise_typeerror_hei(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(10, "2")
        str_err = "height must be an integer"
        self.assertRegex(str(e.exception), str_err)

    def test_raise_ty_err_width(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle("10", 2)
        str_err = "width must be an integer"
        self.assertRegex(str(e.exception), str_err)

    def test_raise_ty_err_x(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(10, 2, True, 0, 4)
        str_err = "x must be an integer"
        self.assertRegex(str(e.exception), str_err)

    def test_raise_ty_err_y(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, 2, 0, [3, 5], 103)
        str_err = "y must be an integer"
        self.assertRegex(str(e.exception), str_err)

    def test_raise_value_error_width(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(10, 2)
            r1.width = -10
        str_err = "width must be > 0"
        self.assertRegex(str(e.exception), str_err)

    def test_raise_value_error_hei(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(10, 2)
            r1.height = -10
        str_err = "height must be > 0"
        self.assertRegex(str(e.exception), str_err)

    def test_raise_value_error_x(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(10, 2)
            r1.x = -10
        str_err = "x must be >= 0"
        self.assertRegex(str(e.exception), str_err)

    def test_raise_value_error_y(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(10, 2)
            r1.y = -10
        str_err = "y must be >= 0"
        self.assertRegex(str(e.exception), str_err)

    def test_area(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)

    def test_display(self):
        r1 = Rectangle(2, 3, 2, 2)
        cap_stdo = io.StringIO()
        with patch('sys.stdout', new=cap_stdo):
            r1.display()
        output = cap_stdo.getvalue()
        self.assertEqual(output, "\n\n  ##\n  ##\n  ##\n")

    def test_update_outp(self):
        r1 = Rectangle(10, 10, 10, 10)
        cap_stdo = io.StringIO()
        with patch("sys.stdout", new=cap_stdo):
            print(r1)
        output = cap_stdo.getvalue()
        self.assertEqual(output.strip(), "[Rectangle] (1) 10/10 - 10/10")


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""
Module of an empty class BaseGeometry
"""


class BaseGeometry:
    """
    the class BaseGeometry is a child of the class dictionnary
    """
    def __init__(self, base_area=None):
        """
        the constructor
        """
        self.base_area = base_area

    def area(self):
        """
        the function area that returns the area or raise error
        """
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()
    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

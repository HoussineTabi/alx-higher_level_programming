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
        if self.base_area is None:
            raise Exception("area() is not implemented")
        else:
            return self.base_area

    def integer_validator(self, name, value):
        """
        this method implements the name and the value
        """
        self.name = name
        if isinstance(value, int):
            if value > 0:
                self.value = value
            else:
                raise ValueError("{} must be greater than 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))


if __name__ == "__main__":

    import doctest
    doctest.testfile("./tests/7-base_geometry.txt")
    bg = BaseGeometry()
    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)
    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

#!/usr/bin/python3
"""
Module of an empty class Rectangle that inherits from BaseGeometry
"""


class Rectangle(__import__("7-base_geometry").BaseGeometry):
    """
    the class BaseGeometry is a child of the class dictionnary
    """
    def __init__(self, width, height):
        """
        the constructo
        """
        if width >= 0 and height >= 0:
            self.__width = width
            self.__height = height
        else:
            if width < 0:
                raise TypeError("with must be an integer")
            else:
                raise TypeError("height must be an integer")

    def area(self):
        """
        returns the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        the form of the Rectangle
        """
        class_name = self.__class__.__name__
        return "[{}] {}/{}".format(class_name, self.__width, self.__height)


class Square(Rectangle):
    """
    This class define
    """

    def __init__(self, size):
        Rectangle.__init__(self, size, size)


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())

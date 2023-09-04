#!/usr/bin/python3
"""
In this module we create a class to define a Rectangle
"""


class Rectangle:
    """
    In this class we dfine a Rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        gets the value of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the value of the width
        """
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        gets the value of the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value of the height
        """
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)

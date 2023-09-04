#!/usr/bin/python3
"""
In this module we create a class to define a Rectangle
"""


class Rectangle:
    """
    In this class we dfine a Rectangle
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def width(self):
        return self.__with
    @width.setter
    def width(self, value):
        self.__width = value
    @proprety



if __name__ == "__main__":
    my_rectangle = Rectangle()
    print(my_rectangle)
    print(my_rectangle.__dict__)

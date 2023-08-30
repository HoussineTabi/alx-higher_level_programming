#!/usr/bin/python3
"""
This class is used to Create object of type Square
"""


class Square:
    """
    This class is used to define a square object
    """
    def __init__(self, size=0):
        """
        This mothod initialize an object of the class square
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size mst be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        calculate the area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        get the value of the private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size is function sets a value in the attribute size
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """
        print a square in the stdout with #
        """
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()

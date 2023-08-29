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
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

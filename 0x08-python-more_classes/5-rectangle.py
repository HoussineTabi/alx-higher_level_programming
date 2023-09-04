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

    def area(self):
        """
        returns the area of a Rectangle object
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        returns the perimeter of a Rectangle object
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        returns a simple representation of an object the frome
        """
        sheap = ''
        if self.__width == 0 or self.height == 0:
            return sheap
        for i in range(self.__height):
            if i != self.__height - 1:
                sheap += "#" * self.__width + "\n"
            else:
                sheap += "#" * self.__width
        return sheap

    def __repr__(self):
        """
        returns a simple representation of an object
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        prints Bye rectangle... when a Rectangle is deleted
        """
        print("Bye rectangle...")


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    del my_rectangle

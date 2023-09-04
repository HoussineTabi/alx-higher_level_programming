#!/usr/bin/python3
"""
In this module we create a class to define a Rectangle
"""


class Rectangle:
    """
    In this class we dfine a Rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        creates an instance
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

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
                sheap += str(self.print_symbol) * self.__width + "\n"
            else:
                sheap += str(self.print_symbol) * self.__width
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
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)


if __name__ == "__main__":
    rect = Rectangle()

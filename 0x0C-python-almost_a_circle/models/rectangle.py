#!/usr/bin/python3
"""
The rectangle module
"""
import base
Base = base.Base


class Rectangle(Base):
    """
    the rectanle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialize a rectangle
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or issubclass(type(value), bool):
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or issubclass(type(value), bool):
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int) or issubclass(type(value), bool):
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int) or issubclass(type(value), bool):
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

    def area(self):
        """
        returns the area of a Rectangle
        """
        return (self.width * self.height)

    def display(self):
        rectangle = ''
        if self.height == 0 or self.width == 0:
            print()
            return
        rectangle += '\n' * self.__y
        for i in range(self.height):
            if i != self.height - 1:
                rectangle += ' ' * self.x + self.width * '#' + '\n'
            else:
                rectangle += ' ' * self.x + self.width * '#'
        print(rectangle)

    def __str__(self):
        iden = self.id
        wid = self.width
        hei = self.height
        x = self.x
        y = self.y
        cl_nm = self.__class__.__name__
        string = "[{}] ({}) {}/{} - {}/{}".format(cl_nm, iden, x, y, wid, hei)
        return string

    def update(self, *args, **kwargs):
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                    continue
                if i == 1:
                    self.width = args[i]
                    continue
                if i == 2:
                    self.height = args[i]
                    continue
                if i == 3:
                    self.x = args[i]
                    continue
                if i == 4:
                    self.y = args[i]
        else:
            attributes = ["id", "width", "height", "x", "y"]
            for key in kwargs:
                for i in range(len(attributes)):
                    if attributes[i] == key and isinstance(key, str):
                        if i == 0:
                            self.id = kwargs[attributes[i]]
                        elif i == 1:
                            self.width = kwargs[attributes[i]]
                        elif i == 2:
                            self.height = kwargs[attributes[i]]
                        elif i == 3:
                            self.x = kwargs[attributes[i]]
                        elif i == 4:
                            self.y = kwargs[attributes[i]]

    def to_dictionary(self):
        obj_dict = {"id": self.id, "height": self.height, "width": self.width}
        obj_dict["x"] = self.x
        obj_dict["y"] = self.y
        return obj_dict


if __name__ == "__main__":
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

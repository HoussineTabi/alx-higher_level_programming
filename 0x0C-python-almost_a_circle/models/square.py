#!/usr/bin/python3
"""
The square module
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    The square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)
        self.__size = size

    def __str__(self):
        name = self.__class__.__name__
        size = self.width
        iden = self.id
        x = self.x
        y = self.y
        return "[{}] ({}) {}/{} - {}".format(name, iden, x, y, size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                    self.width = args[i]
                    self.heigtht = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size" and isinstance(key, str):
                    self.size = kwargs[key]
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                elif key == "x" and isinstance(key, str):
                    self.x = kwargs[key]
                elif key == 'y' and isinstance(key, str):
                    self.y = kwargs[key]

    def to_dictionary(self):
        square_dict = dict()
        square_dict["id"] = self.id
        square_dict["size"] = self.size
        square_dict["x"] = self.x
        square_dict["y"] = self.y
        return square_dict


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

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

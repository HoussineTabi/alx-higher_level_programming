#!/usr/bin/python3
"""
module for the inheritance
"""


class MyList(list):
    """
    Myclass is a class that inherits from list
    """

    def print_sorted(self):
        """
        prints the object in a sorted order
        """
        print(sorted(MyList(self)))


if __name__ == "__main__":
    my_list = MyList()

#!/usr/bin/python3
"""
this module of the class student
"""


class Student:
    """
    the student class
    """

    def __init__(self, first_name, last_name, age):
        """
        instantiation method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        to_json method
        """
        return self.__dict__


if __name__ == "__main__":
    print()

#!/usr/bin/python3
"""
the module of the task number 10
"""


class Student:
    """
    This class represent the student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            rdic = self.__dict__.items()
            return {k: v for k, v in rdic if key in attrs}


if __name__ == "__main__":
    print()

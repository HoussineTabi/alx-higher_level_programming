#!/usr/bin/python3
"""
this module of the class student
"""


class Stduent:
    """
    the student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @staticmethod
    def to_json(self):
        dic = self.__dict__
        student_dict = {}
        for i, j in dic.items():
            if isinstance(j, (list, tuple, dict, str, int, bool)):
                student_dict[i] = j
        return student_dict


if __name__ == "__main__":
    print()

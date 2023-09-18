#!/usr/bin/python3
"""
the Base module
"""
import json


class Base:
    """
    the base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize the object
        """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_of_dict = list()
        filename = cls.__name__ + ".json"
        if list_objs is None:
            with open(filename, "w+", encoding="utf-8") as f:
                json.dump([], f)
        else:
            for i in list_objs:
                list_of_dict.append(i.to_dictionary())
            with open(filename, "w+", encoding="utf-8") as f:
                json.dump(list_of_dict, f)

    @staticmethod
    def from_json_string(json_string):
        list_of_objs = list()
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary is None:
            return {}
        if cls.__name__ == "Rectangle":
            obj = cls(dictionary["width"], dictionary['height'])
            obj.update(**dictionary)
        elif cls.__name__ == "Square":
            obj = cls(dictionary['size'])
            obj.update(**dictionary)
        else:
            obj = cls()
        return (obj)

    @classmethod
    def load_from_file(cls):
        """
        load json from a file
        """
        filename = cls.__name__ + '.json'
        obj = []
        list_of_obj = list()
        with open(filename, encoding='utf-8') as f:
            string = f.read()
            if len(string) == 0 or string is None:
                return []
            obj = json.loads(string)
            for ele in obj:
                list_of_obj.append(cls(**ele))

        return list_of_obj

    def __del__(self):
        Base.__nb_objects -= 1


if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b4 = Base(12)
    print(b4.id)

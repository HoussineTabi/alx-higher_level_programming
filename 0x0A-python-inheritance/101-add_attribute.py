#!/usr/bin/python3
"""
module to add an attribute to an object if possible
"""


def add_attribute(obj, name, name_value):
    """
    this function adds an attribute to an object if it's possible
    """
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, name_value)

if __name__ == "__main__":
    class MyClass():
        pass
    
    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

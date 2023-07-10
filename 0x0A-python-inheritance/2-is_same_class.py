#!/usr/bin/python3
"""defines a class-checking function"""

def is_same_class(obj, a_class):
    """check if an object is exactly an instance of given class

    Args:
    obj (any): The obj to check.
    a_class (type): The class to match the type of obj
    Returns:
    if obj is exactly an instance of a_class - True
    otherwise - false
    """
    if type(obj) == a_class:
        return True
    return False


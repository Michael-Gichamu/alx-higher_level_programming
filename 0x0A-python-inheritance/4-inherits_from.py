#!/usr/bin/python3

"""
This module defines a function that checks only sub class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        obj (object): Object to check.
        a_class (class): Specified class.

    Returns:
        if obj is a subclass of a_class - True.
        Otherwise - False.
    """
    obj_class = type(obj)
    if issubclass(obj_class, a_class) and obj_class != a_class:
        return True
    return False

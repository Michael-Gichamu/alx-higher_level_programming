#!/usr/bin/python3

"""
This module provides a function that checks object.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class.

    Args:
        obj (object): Object to check.
        a_class (class): The specified class.

    Returns:
         if the object is an instance of, or if the object
            is an instance of a class that inherited from - True.
         Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False

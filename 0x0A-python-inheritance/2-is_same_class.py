#!/usr/bin/python3

"""
This module provides a function that checks if
object is an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if object is exactly an instance of the specified class

    Args:
        obj (object): The object to be checked.
        a_class (class): specified class.

    Returns:
        if obj is exactly an instance of a_class - True
        Otherwise - False
    """
    if type(obj) == a_class:
        return True
    else:
        return False

#!/usr/bin/python3

"""
This module provides a function that checks if
object is an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if object is exactly an instance of the specified class

    Args:
        obj (any): The object to be checked.
        a_class (class): specified class.

    return:
        if obj is an instance - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

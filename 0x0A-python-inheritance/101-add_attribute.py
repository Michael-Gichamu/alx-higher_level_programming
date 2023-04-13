#!/usr/bin/python3
"""
Defines add_attribute function.
"""


def add_attribute(obj, name, value):
    """
    Adds attribute to an object.

    Args:
        obj (object): Object.
        name (key): Attribute name.
        value (value): Value
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value

#!/usr/bin/python3

"""
This module provides a function that prints first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints name passed to the function.

    Args:
        first_name (int)
        last_name (int)
    raises:
        TypeError if name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

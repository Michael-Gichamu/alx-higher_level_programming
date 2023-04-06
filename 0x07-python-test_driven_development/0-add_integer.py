#!/usr/bin/python3

"""Funtion adds two integers"""

def add_integer(a, b=98):
    """
    This function adds of two numbers.

    Args:
        a (int): The first number to add.
        b (int): The second number to add.

    Returns:
        The sum of x and y (int).
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

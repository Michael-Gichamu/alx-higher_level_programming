#!/usr/bin/python3

"""
This module provides a function that prints a square with the character #.
"""


def print_square(size):
    """
    Prints a square with character #.

    Args:
        size (int): length of the square.
    
    Raise:
        TypeError: size is not integer.
        ValueError: size is less than zero.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

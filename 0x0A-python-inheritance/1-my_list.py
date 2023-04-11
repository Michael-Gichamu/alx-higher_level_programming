#!/usr/bin/python3

"""
Defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    Inherits class list,
    Print a list in ascending order.
    """
    def print_sorted(self):
        print(sorted(self))

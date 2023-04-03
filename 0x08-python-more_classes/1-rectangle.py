#!/usr/bin/python3
# 1-rectangle.py
# Michael Gichamu
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle Oonject with the given width and height

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Default to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width == value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

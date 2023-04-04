#!/usr/bin/python3
# 1-rectangle.py
# Michael Gichamu
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle Object with the given width and height

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Default to 0.
        """
        self.width = width
        self.height = height

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
        self.__width = value

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
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""

        string = ""
        for i in range(self.height):
            for j in range(self.width):
                string += "#"
            string += "\n"
        return string[:-1]

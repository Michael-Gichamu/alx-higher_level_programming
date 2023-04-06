#!/usr/bin/python3

"""
This module provides the function that divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor

    Args:
        matrix (list of lists): The matrix with its elements to be divided.
        div (int or float): Divisor by which the element is divide by.

    Return:
        A new matrix with the elements divided, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
                or div is not an integer/float.
        ZeroDivisionError: If div is zero.
    """

    if not isinstance(matrix, list) or matrix == [] or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item/div, 2) for item in row] for row in matrix]

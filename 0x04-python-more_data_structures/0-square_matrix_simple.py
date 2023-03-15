#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        square_row = []
        for element in row:
            square_row.append(element**2)
        square_matrix.append(square_row)
    return square_matrix

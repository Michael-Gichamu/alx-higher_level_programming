#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        row_len = len(matrix[i])
        for j in range(row_len):
            if j != row_len - 1:
                endCh = ' '
            else:
                endCh = ''
            print("{:d}".format(matrix[i][j]), end=endCh)
        print("")

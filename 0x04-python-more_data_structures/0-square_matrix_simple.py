#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """this function calculate the square of elements
       of a matrix and returns them as a new matrix
       Arguments:
                 matrix: the matrix that we want to calculate the
                         the square of each value
                 Return: the new matrix with the square of eache value
    """
    new_matrix = []
    for i in matrix:
        line = []
        for j in i:
            line.append(j)
        new_matrix.append(line)
    return (new_matrix)

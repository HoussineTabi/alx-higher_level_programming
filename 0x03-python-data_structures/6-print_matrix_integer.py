#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """print a matrix of integer
       Arguments:
                 matrix: the matrix of integer
    """
    for i in matrix:
        for j in range(len(i) - 1):
            print("{:d}".format(i[j]), end=' ')
        print("{:d}".format(i[len(i) - 1]))

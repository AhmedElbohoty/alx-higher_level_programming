#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    '''Prints a matrix of integers.
    '''

    if matrix == [[]]:
        print("")

    for arr in matrix:
        for idx, x in enumerate(arr):
            if idx != len(arr) - 1:
                print("{:d}".format(x), end=" ")
            else:
                print("{:d}".format(x))

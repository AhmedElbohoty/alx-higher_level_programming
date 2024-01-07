#!/usr/bin/python3
'''Module for dividing all elements of a matrix

Functions:
    matrix_divided
'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix.

    Args:
        1- matrix (obj: lists): list of lists of integers or floats
        2- div (int): the divisor

    Raises:
        TypeError: if matrix is not a list of lists of integers or floats
                   'matrix must be a matrix (list of lists) of integers/floats'
        TypeError: if each row of the matrix are not the same size
                   'Each row of the matrix must have the same size'
        TypeError: if div is not a number (integer or float)
                   'div must be a number'
        ZeroDivisionError: if div equals zero
                           'division by zero'

    Returns:
        returns matrix consists of results of division
    '''
    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    if matrix == []:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        for numb in row:
            if not isinstance(numb, (int, float)):
                raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats')

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(numb / div, 2) for numb in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

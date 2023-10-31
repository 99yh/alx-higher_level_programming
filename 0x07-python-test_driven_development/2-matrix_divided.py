#!/usr/bin/python3
"""Matrix Division Module.

This module provides a function to divide a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Divide a matrix by a number.

    Arguments
    ---------
    matrix: list of lists of integers
        Each list inside should have the same size
    number: integer or float
        Number should be any number except zero

    Return
    ------
    another_matrix: list of lists of integers
        Holds the results of dividing each element of the
        given matrix by the given number, it has the same
        size of the given matrix, and the elements inside
        it is rounded  to 2 decimal  places, this  one is
        defferent form the given matrix
    """
    new_mtx = []
    matrix_check(matrix, div)
    for idx, row in enumerate(matrix):
        new_mtx.append([])
        for elem in row:
            new_mtx[idx].append(round(elem/div, 2))
    return new_mtx


def matrix_check(matrix, div=1):
    """
    Check if ``matrix`` is valid

    Raises
    ------
    ZeroDivisionError: ``div`` is zero.
    TypeError: ``div`` or any element of the ``matrix`` is not a number
    TypeError: rows in ``matrix`` does not have the same size
    """
    siz = -1
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if siz == -1:
            siz = len(row)
        elif siz != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

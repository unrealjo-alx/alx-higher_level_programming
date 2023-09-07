#!/usr/bin/python3
"""
2-matrix_divided.py : matrix_divided()
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number, rounded to 2 decimal places.

    Args:
        matrix (list of lists): : A matrix of integers or floats.
        div (number): The number to divide the elements of the matrix by.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
        or if div is not a number.
        TypeError: If any row of the matrix has a different length than the others.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists: A new matrix
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row)
        for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if all(len(row) == matrix[0] for row in matrix) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]

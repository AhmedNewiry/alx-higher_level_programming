#!/usr/bin/python3
""" a module containing matrix_divided fucntion"""


def matrix_divided(matrix, div):
    """ a funciton that divides all list element 
        in a matrix by an integer
        Args:
            matrix (list): a list of lists of integers/flaots
            div (int): the divisor
        Returns:  a new matrix
    """
    if not type(matrix) is list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for m_list in matrix:
        if not type(m_list) is list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not all(type(item) is int for item in m_list) \
        and not all(type(item) is float for item in m_list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(m_list) == len(matrix[0]) for m_list in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not type(div) is int and not type(div) is float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in m_list] for m_list in matrix]

#!/usr/bin/python3

def return_square(list_t):

    return [i**2 for i in list_t]

def square_matrix_simple(matrix=[]):
    return list(map(return_square, matrix))

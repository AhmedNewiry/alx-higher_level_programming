#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return list(map(lambda list_t: [i**2 for i in list_t], matrix))

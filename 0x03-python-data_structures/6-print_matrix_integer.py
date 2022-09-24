#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list_x in matrix:
        for item in list_x:
            print("{:d} ".format(item),end="")
        print('') 

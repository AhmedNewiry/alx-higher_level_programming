#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list_x in matrix:
        for i in range(len(list_x)):
            print("{:d} ".format(list_x[i]),end="")
        print("")

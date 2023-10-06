#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for _list in matrix:
        for i in _list[:-1]:
            print("{:d}".format(i), end=" ")
        if _list:
            print("{:d}".format(_list[-1]))
        else:
            print()

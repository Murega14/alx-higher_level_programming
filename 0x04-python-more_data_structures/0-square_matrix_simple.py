#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lamda x: x * x, row)) for row in matrix])

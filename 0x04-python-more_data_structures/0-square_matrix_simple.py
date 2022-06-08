#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    r = []
    for y in matrix:
        r.append([e * e for e in y])
    return r

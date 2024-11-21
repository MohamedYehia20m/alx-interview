#!/usr/bin/python3


"""
    rotate_2d_matrix module
    rotate n x n 2D matrix 90 degrees clockwise.
"""
def rotate_2d_matrix(matrix):
    matrix[:] = zip(*matrix[::-1])

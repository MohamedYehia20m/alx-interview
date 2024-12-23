#!/usr/bin/python3
"""
rotate_2d_matrix module
Rotates a n x n 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a square 2D matrix in place 90 degrees clockwise.

    Args:
        matrix (list[list[int]]): The n x n 2D matrix to rotate.

    Returns:
        None: The matrix is modified in place.
    """
    matrix[:] = [list(row) for row in zip(*matrix[::-1])]

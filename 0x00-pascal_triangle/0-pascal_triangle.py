#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Create a function def pascal_triangle(n): that returns
    a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = [[1]]

    # looping rows from 1 to n -1
    for i in range(1, n):
        row = []

        row.append(1)  # start
        # looping row cells to fill it with values
        for j in range(i - 1):  # for row no.2 we fill one cell with index 0.
            row.append(triangle[i-1][j] + triangle[i-1][j + 1])
        row.append(1)  # end
    triangle.append(row)
    return triangle

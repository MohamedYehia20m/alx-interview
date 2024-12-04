#!/usr/bin/python3
"""
Module: island_perimeter
This module calculates the perimeter of an island in a given grid.
Each cell in the grid is either land (1) or water (0), and the goal is to
determine the perimeter of the island formed by the land cells.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    This function traverses through the grid, and for each land cell (1),
    it adds 4 to the perimeter. Then it subtracts 2 for each adjacent land
    cell (above or left) to avoid double counting the shared borders.

    Args:
        grid (list of list of int): A 2D grid representing the map where
                                     1 indicates land and 0 indicates water.

    Returns:
        int: The perimeter of the island formed by the land cells.

    Example:
        grid = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        island_perimeter(grid) -> 16
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4
                # Check for adjacent land
                # (only above and left to avoid redundancy)
                if i > 0 and grid[i - 1][j] == 1:
                    # Subtract 2 for shared border with the cell above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    # Subtract 2 for shared border with the cell to the left
                    perimeter -= 2

    return perimeter

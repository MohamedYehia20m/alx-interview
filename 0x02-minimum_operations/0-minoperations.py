#!/usr/bin/python3

"""
min_operations.py

This module provides a function to calculate the minimum number of operations
needed to create a string of 'H' characters using two operations: Copy All
and Paste. Starting with a single 'H', the goal is to reach a target number
of 'H' characters specified by the user.

Functions:
----------
minOperations(n): Calculates the minimum number of operations to obtain n 'H'
characters. Returns the number of operations
or 0 if n is less than or equal to 1.

Usage:
------
To use this module, simply call the minOperations function with an integer
parameter representing the desired number of 'H' characters:

    result = minOperations(8)
    print(f"Minimum operations to obtain 8 'H's: {result}")
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to obtain n 'H' characters
    starting from 1 'H' using two operations: Copy All and Paste.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed to reach n,
         or 0 if it's not possible.
    """
    if n <= 1:
        return 0

    op = 0  # Initialize the operation counter
    mul_factor = 1  # Factor to multiply by (the last copy)
    num = 1  # Current number of 'H' characters

    while num < n:
        if n % num == 0:
            mul_factor = num
            num *= 2
            op += 2  # Copy All and Paste
        else:
            num += mul_factor
            op += 1  # Paste

    if num == n:
        return op
    else:
        return 0

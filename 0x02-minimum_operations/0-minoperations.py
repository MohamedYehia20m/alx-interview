#!/usr/bin/python3


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

#!/usr/bin/python3
"""
Module: make_change
This module provides a function to calculate the minimum number of coins
needed to meet a given total using a set of coin denominations.
"""

def makeChange(coins, total):
    """
    Calculate the minimum number of coins required to meet a given total.

    Args:
        coins (list): List of coin denominations (positive integers).
        total (int): The target amount to achieve with the coins.

    Returns:
        int: Minimum number of coins needed, or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    remainder = total
    result = 0

    coins.sort(reverse=True)  # Sort descending

    for unit in coins:
        if remainder == 0:
            break
        result += remainder // unit
        remainder %= unit

    return result if remainder == 0 else -1

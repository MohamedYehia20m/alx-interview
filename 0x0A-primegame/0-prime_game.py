#!/usr/bin/python3
"""
Prime Game Module.

This module defines a game played between two players, 'Maria' and 'Ben',
over multiple rounds. In each round, players consider all prime numbers up to
a given integer `n`. The player who can pick the last prime wins that round.

The winner of the game is determined by counting the number of rounds each
player wins. If the number of prime numbers up to `n` is odd, Maria wins
the round if the count is even, Ben wins.

Functions:
    - isWinner(x, nums): Determines the overall winner of the game.
    - count_primes(n): Counts the number of prime numbers up to a given number.
    - is_prime(num): Checks whether a given number is prime.

Usage:
    >>> isWinner(3, [4, 5, 6])
    'Maria'
"""


def isWinner(x, nums):
    """
    Determines the overall winner of the prime number game.

    The game consists of `x` rounds. For each round, players consider all prime
    numbers up to a given integer `num` (from the `nums` list). The player who
    wins the majority of the rounds is declared the overall winner.

    Rules:
    - If the number of prime numbers up to `num` is odd, Maria wins the round.
    - If the number of prime numbers up to `num` is even, Ben wins the round.

    :param x: (int) Number of rounds to be played.
    :param nums: (list of int) List of integers, where each integer specifies
                 the upper limit for prime counting in a given round.
    :return: (str or None) Returns:
             - 'Maria' if Maria wins more rounds.
             - 'Ben' if Ben wins more rounds.
             - None if there is a tie.

    Example:
    >>> isWinner(3, [4, 5, 6])
    'Maria'
    """
    ben = 0  # Counter for Ben's wins
    maria = 0  # Counter for Maria's wins

    for num in nums:
        prime_count = count_primes(num)  # Count the primes up to 'num'
        if prime_count % 2 == 0:  # Even count --> Ben wins
            ben += 1
        else:  # Odd count --> Maria wins
            maria += 1

    # Determine overall winner based on win counts
    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None


def count_primes(n):
    """
    Counts the total number of prime numbers from 1 to `n` (inclusive).

    A prime number is a positive integer greater than 1 that has no divisors
    other than 1 and itself.

    :param n: (int) Upper limit for counting primes.
    :return: (int) The total number of prime numbers between 1 and `n`.

    Example:
    >>> count_primes(10)
    4
    (Prime numbers are: 2, 3, 5, 7)
    """
    count = 0  # Prime counter
    for i in range(2, n + 1):  # Check numbers from 2 to n
        if is_prime(i):  # If i is prime, increment the counter
            count += 1
    return count


def is_prime(num):
    """
    Determines if a given number is prime.

    A prime number is a natural number greater than 1 that is only divisible by
    1 and itself. To optimize, this function checks divisors up to the square
    root of the number.

    :param num: (int) The number to check for primality.
    :return: (bool) True if `num` is prime, False otherwise.

    Example:
    >>> is_prime(7)
    True
    >>> is_prime(4)
    False
    """
    if num < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, int(num**0.5) + 1):  # Check divisors up to √num
        if num % i == 0:  # If divisible, not prime
            return False
    return True

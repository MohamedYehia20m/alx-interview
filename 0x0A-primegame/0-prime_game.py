#!/usr/bin/python3


def isWinner(x, nums):
    """
    Determines the winner of the game.

    :param x: Number of rounds.
    :param nums: List of integers for each round.
    :return: The name of the winner ('Ben', 'Maria') or None.
    """
    ben = 0
    maria = 0

    for num in nums:
        prime_count = count_primes(num)
        if prime_count % 2 == 0:  # Even count --> Ben wins
            ben += 1
        else:  # Odd count --> Maria wins
            maria += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None


def count_primes(n):
    """
    Counts the number of prime numbers up to n (inclusive).

    :param n: Upper limit.
    :return: Count of prime numbers.
    """
    count = 0
    for i in range(2, n + 1):  # num is included
        if is_prime(i):
            count += 1
    return count


def is_prime(num):
    """
    Checks if a number is prime.

    :param num: Number to check.
    :return: True if prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of a prime game between 'Maria' and 'Ben'.

    In each round, the player who can pick the last prime number wins the round.
    Maria wins if the count of prime numbers up to `num` is odd; otherwise, Ben wins.

    :param x: (int) Number of rounds to be played.
    :param nums: (list) List of integers, where each element represents the range `n`
                 for a round. For each round, the prime numbers up to `n` are counted.
    :return: (str or None) The name of the overall winner ('Ben' or 'Maria') based on
             who wins more rounds. If there is a tie, it returns `None`.
    
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
    Counts the number of prime numbers from 1 to `n` (inclusive).

    A prime number is a natural number greater than 1 that has no divisors 
    other than 1 and itself.

    :param n: (int) Upper limit for counting primes.
    :return: (int) The total number of prime numbers from 1 to `n`.

    Example:
    >>> count_primes(10)
    4
    (Prime numbers: 2, 3, 5, 7)
    """
    count = 0  # Prime counter
    for i in range(2, n + 1):  # Check numbers from 2 to n
        if is_prime(i):  # If i is prime, increment the counter
            count += 1
    return count


def is_prime(num):
    """
    Determines if a given number is prime.

    A prime number is only divisible by 1 and itself. The function checks divisors 
    up to the square root of `num` for efficiency.

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
    for i in range(2, int(num**0.5) + 1):  # Check for factors up to √num
        if num % i == 0:  # If divisible, not prime
            return False
    return True

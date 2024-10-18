#!/usr/bin/python3
"""
Prime Game simulation between Maria and Ben.
"""


def primes(n):
    """
    Return a list of prime numbers between 1 and n inclusive.

    Args:
        n (int): The upper boundary of the range, where the lower boundary
                 is always 1.

    Returns:
        list: A list of prime numbers within the range from 1 to n.
    """
    prime = []
    sieve = [True] * (n + 1)

    for p in range(2, n + 1):
        if sieve[p]:
            prime.append(p)
            for i in range(p * 2, n + 1, p):
                sieve[i] = False

    return prime


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): The number of rounds of the game.
        nums (list of int): Upper limits for each round of the game.

    Returns:
        str: The name of the winner ("Maria" or "Ben"). If no winner is
             determined, returns None.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    Maria = Ben = 0  # Initialize counters for wins

    # Calculate the number of wins per round for Maria and Ben
    for round_num in range(x):
        prime_list = primes(nums[round_num])
        if len(prime_list) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    # Determine the overall winner
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    else:
        return None

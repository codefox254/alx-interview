#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Returns a list of booleans indicating prime numbers up to n"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for start in range(2, int(n ** 0.5) + 1):
        if sieve[start]:
            for i in range(start * start, n + 1, start):
                sieve[i] = False
    return sieve

def count_primes_up_to(n, prime_sieve):
    """Counts the number of primes up to n using the sieve"""
    return sum(prime_sieve[:n + 1])

def isWinner(x, nums):
    """
    Determines the winner of x rounds of the prime game.
    Maria always goes first, both players play optimally.
    
    Arguments:
    - x: number of rounds
    - nums: array where each element is the 'n' for each round
    
    Returns:
    - Name of the player with the most wins (Maria or Ben), or None if tie.
    """
    if not nums or x < 1:
        return None
    
    max_n = max(nums)
    prime_sieve = sieve_of_eratosthenes(max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        prime_count = count_primes_up_to(n, prime_sieve)
        # If prime_count is odd, Maria wins, if even, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

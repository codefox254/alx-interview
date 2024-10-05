#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """
    Generate a sieve of primes up to n.
    Args:
    n (int): upper limit for prime numbers
    
    Returns:
    list: A list where True indicates that the index is a prime number.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return sieve

def isWinner(x, nums):
    """
    Determine the winner of x rounds of the prime game.
    
    Args:
    x (int): the number of rounds
    nums (list of int): array where each element represents the upper limit n for that round
    
    Returns:
    str: the name of the player with the most wins (Maria or Ben), or None if there's a tie
    """
    if not nums or x < 1:
        return None
    
    # Maximum value of n in nums, to generate sieve up to this value
    max_n = max(nums)
    
    # Generate primes up to the largest number in nums
    prime_sieve = sieve_of_eratosthenes(max_n)
    
    # Precompute the number of primes up to each number in nums
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if prime_sieve[i] else 0)
    
    maria_wins = 0
    ben_wins = 0
    
    # For each round, determine who wins based on the number of primes up to nums[i]
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

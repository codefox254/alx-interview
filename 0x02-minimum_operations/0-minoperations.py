#!/usr/bin/python3
"""
This module provides a function minOperations to calculate the fewest number
of operations needed to result in exactly n H characters in a file.
The only operations allowed are "Copy All" and "Paste".

Author: Your Name
"""

def minOperations(n):
    """
    Calculate the minimum number of operations to get exactly n H characters.

    Args:
        n (int): The number of H characters desired.

    Returns:
        int: The minimum number of operations required.
             If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

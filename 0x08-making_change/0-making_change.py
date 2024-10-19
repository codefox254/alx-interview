#!/usr/bin/python3
""" Making changes using Dynamic Programming """


def makeChange(coins, total):
    """ Generate the fewest number of coins needed to meet total

    Args:
        coins (List[int]): List of coins available
        total (int): total amount needed
    Returns:
        int: fewest number of coins needed to meet total, or -1 if not possible
    """
   if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count

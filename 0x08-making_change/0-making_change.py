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

    # Initialize DP array to store minimum coins required for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make a total of 0

    # Iterate over each coin
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[total] is still infinity, return -1 because total can't be reached
    return dp[total] if dp[total] != float('inf') else -1

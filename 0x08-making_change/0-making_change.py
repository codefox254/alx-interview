#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create a DP array to store the fewest coins for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin and calculate the minimum coins required
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

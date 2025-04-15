def coin_change_recursive(coins, amount, memo={}):
    """
    Solves the coin change problem using recursion with memoization.

    Args:
        coins: A list of coin denominations.
        amount: The target amount.
        memo: A dictionary to store results of subproblems.

    Returns:
        The minimum number of coins needed to make the amount, or -1 if it's not possible.
    """
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if amount in memo:
        return memo[amount]

    min_coins = float('inf')
    for coin in coins:
        result = coin_change_recursive(coins, amount - coin, memo)
        if result != -1:
            min_coins = min(min_coins, result + 1)

    memo[amount] = min_coins if min_coins != float('inf') else -1
    return memo[amount]


# Example usage:
coins = [1, 2, 5]
amount = 11
result = coin_change_recursive(coins, amount)
print(f"Minimum coins needed for {amount}: {result}")  # Output: 3

coins = [2]
amount = 3
result = coin_change_recursive(coins, amount)
print(f"Minimum coins needed for {amount}: {result}")  # Output: -1
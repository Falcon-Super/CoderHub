def coins_combinations(amount, coins):
    # Initialize the list with zeros up to the target amount
    combinations = [0] * (amount + 1)

    # There is one combination for zero amount
    combinations[0] = 1

    # Iterate over the coins and update the combinations list
    for coin in coins:
        for i in range(coin, amount + 1):
            combinations[i] += combinations[i - coin]

    # Return the number of possible combinations for the target amount
    return combinations[amount]

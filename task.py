def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    change = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            change[coin] = count
            amount -= count * coin

    return change



def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    change = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in change:
            change[coin] += 1
        else:
            change[coin] = 1
        
        amount -= coin

    return change


amount = 649
print(find_coins_greedy(amount))
print(find_coins_greedy(amount))



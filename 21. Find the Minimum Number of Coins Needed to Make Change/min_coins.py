from math import inf


def min_coins(amount, coins):

    dp = [inf for _ in range(amount + 1)]
    dp[0] = 0

    for x in range(1, amount + 1):
        for c in coins:
            if x - c >= 0:
                dp[x] = min(dp[x], dp[x - c] + 1)

    return dp[amount]


def main():
    
    file = open('rosalind_ba5a.txt', 'r')
    
    amount = int(next(file))
    coins = [int(s) for s in (next(file)).strip().split(',')]

    print(min_coins(amount, coins))


if __name__ == '__main__':
    main()
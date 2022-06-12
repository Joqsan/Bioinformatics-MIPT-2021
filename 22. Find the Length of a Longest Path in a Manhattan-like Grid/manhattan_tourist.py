def manhattan_tourist(n, m, down, right):

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for r in range(1, n+1):
        dp[r][0] = dp[r-1][0] + down[r-1][0]

    for c in range(1, m+1):
        dp[0][c] = dp[0][c-1] + right[0][c-1]

    for r in range(1, n+1):
        for c in range(1, m+1):
            dp[r][c] = max(dp[r-1][c] + down[r-1][c], dp[r][c-1] + right[r][c-1])

    return dp[n][m]


def main():
    
    file = open('rosalind_ba5b.txt', 'r')
    
    n, m = [int(s) for s in next(file).strip().split()]

    down = []
    for _ in range(n):
        row = [int(s) for s in next(file).strip().split()]
        down.append(row)

    next(file)

    right = []
    for _ in range(n+1):
        row = [int(s) for s in next(file).strip().split()]
        right.append(row)

    print(manhattan_tourist(n, m, down, right))


if __name__ == '__main__':
    main()
def MaxTotalWeight(bpWeight, amountGoldIngot, arrWeight):
    n = amountGoldIngot
    dp = [[0] * (bpWeight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w_i = arrWeight[i - 1]
        for w in range(bpWeight + 1):
            dp[i][w] = dp[i - 1][w]  # не брать
            if w_i <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - w_i] + w_i)

    return dp[n][bpWeight]


bpWeight, amount = map(int, input().split())
arrWeight = list(map(int, input().split()))
maxWeight = MaxTotalWeight(bpWeight, amount, arrWeight)
print(maxWeight)
def KnapsackWithoutRepsBU(totalWeight, arrWeight, arrCost):
    maxCostArr = [[0 for _ in range(len(arrWeight) + 1)] for _ in range(totalWeight + 1)]

    for w in range(totalWeight + 1):
        maxCostArr[w][0] = 0

    for i in range(len(arrWeight) + 1):
        maxCostArr[0][i] = 0

    for i in range(1, len(arrWeight) + 1):
        for w in range(1, totalWeight + 1):
            maxCostArr[w][i] = maxCostArr[w][i - 1]
            if arrWeight[i - 1] <= w:
                maxCostArr[w][i] = max(maxCostArr[w][i], maxCostArr[w - arrWeight[i - 1]][i - 1] + arrCost[i - 1])

    return maxCostArr[totalWeight][len(arrWeight)]

weight = int(input())
arrWeight = list(map(int, input().split()))
arrCost = list(map(int, input().split()))
print(KnapsackWithoutRepsBU(weight, arrWeight, arrCost))
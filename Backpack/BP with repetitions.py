def KnapsackWithRepsBU(totalWeight, arrWeight, arrCost):
    maxCostArr = [0] * (totalWeight + 1)
    for w in range(1, totalWeight + 1):
        for i in range(len(arrWeight)):
            if arrWeight[i] <= w:
                maxCostArr[w] = max(maxCostArr[w], maxCostArr[w - arrWeight[i]] + arrCost[i])
    return maxCostArr[totalWeight]

weight = int(input())
arr = list(map(int, input().split()))
arrCost = list(map(int, input().split()))
print(KnapsackWithRepsBU(weight, arr, arrCost))
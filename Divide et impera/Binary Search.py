# .pop() == O(n)

numList = list(map(int, input().split()))
n = numList.pop(0)
numListFind = list(map(int, input().split()))
k = numListFind.pop(0)

resultList = []

for i in range(k):
    left = 0
    right = len(numList) - 1

    while left <= right:
        mid = (left + right) // 2

        if numList[mid] == numListFind[i]:
            resultList.append(mid + 1)
            break
        elif numList[mid] > numListFind[i]:
            right = mid - 1
        else:
            left = mid + 1

        if left > right:
            resultList.append(-1)

print(*resultList)
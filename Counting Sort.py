amount = int(input())
numList = list(map(int, input().split()))

minNum = min(numList)
maxNum = max(numList)
tempList = [0] * (maxNum - minNum + 1)
resultList = []

for j in range(amount):
    tempList[numList[j] - minNum] += 1

for i in range(len(tempList)):
    for _ in range(tempList[i]):
        resultList.append(i + minNum)

print(*resultList)

# ------------------------------

# Версия GPT:

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Шаг 3: Подсчёт количества
    for num in arr:
        count[num] += 1

    # Шаг 4: Префиксная сумма (позиции для вставки)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Шаг 5: Построение отсортированного массива (стабильно)
    output = [0] * len(arr)
    for num in reversed(arr):  # обратный проход важен для стабильности
        pos = count[num] - 1
        output[pos] = num
        count[num] -= 1

    return output


# Пример
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)

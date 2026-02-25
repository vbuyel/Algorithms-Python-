def find_lnds_sequence(arr):
    n = len(arr)
    # Для хранения индексов элементов в подпоследовательности
    prev_indices = [-1] * n
    # Для хранения индексов последних элементов подпоследовательностей разной длины
    tails = []

    for i in range(n):
        # Ищем место для arr[i] в tails с помощью бинарного поиска
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if arr[tails[mid]] >= arr[i]:
                left = mid + 1
            else:
                right = mid

        if left < len(tails):
            tails[left] = i
        else:
            tails.append(i)

        # Записываем предыдущий индекс для восстановления последовательности
        if left > 0:
            prev_indices[i] = tails[left - 1]

    # Восстанавливаем последовательность
    sequence = []
    current = tails[-1]
    while current != -1:
        sequence.append(current + 1)  # +1 для 1-based индексов
        current = prev_indices[current]

    return len(tails), sequence[::-1]


n = int(input())
arr = list(map(int, input().split()))
length, sequence = find_lnds_sequence(arr)

print(length)
print(' '.join(map(str, sequence)))
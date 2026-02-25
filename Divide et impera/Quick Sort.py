import random

def Partition(arr, left, right) -> int:
    index = random.randint(left, right - 1)
    x = arr[index]
    arr[index], arr[left] = arr[left], arr[index]
    j = left

    for i in range(left + 1, right):
        if arr[i] < x:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[left], arr[j] = arr[j], arr[left]

    return j

def QuickSort(arr, left, right) -> list:
    while left < right:
        mid = Partition(arr, left, right)

        # Смотрим, какой отрезок короче для < количества рекурсий
        if mid - left < right - mid:
            QuickSort(arr, left, mid)
            left = mid + 1
        else:
            QuickSort(arr, mid + 1, right)
            right = mid

    return arr

if __name__ == '__main__':
    import numpy as np
    arr = np.arange(1000)
    arr = np.flip(arr)
    print(QuickSort(arr, 0, len(arr)))
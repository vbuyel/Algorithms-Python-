# Input: A[n1, n2, ..., nn]
#
# Output: k-й элемент упорядоченного по неубыванию массива (то есть A'[k])

import random

def RandomSelect(arr, left, right, k):
    if left == right:
        return arr[left]

    # 1. Выбираем случайный элемент
    index = random.randint(left, right - 1)
    x = arr[index]

    # 2. Делим на 3 массива: A[n1, ..., nm1], A[nm1+1, ..., nm2], A[nm2+1, ..., nn]
    #                             < k                == k                 > k
    i = left
    while i <= right:
        if arr[i] < x:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
            i += 1
        elif arr[i] > x:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else:
            i += 1

    # 3. Смотрим, где из 3 массивов находится наше число
    if k < left:
        return RandomSelect(arr, 0, left, k)
    elif k <= right:
        return x
    else:
        return RandomSelect(arr, right + 1, len(arr) - 1, k)

if __name__ == '__main__':
    import numpy as np
    #arr = np.arange(1000)
    #arr = np.flip(arr)
    arr = [3, 4, 7, 1, 4, 2, 9, 0]
    ind = random.randint(0, len(arr) - 1)
    print(ind)
    print(RandomSelect(arr, 0, len(arr) - 1, ind))
def Partition(arr, left, right, elem) -> int:
    x = arr[left][elem]
    j = left

    for i in range(left + 1, right + 1):
        if arr[i][elem] < x:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[left], arr[j] = arr[j], arr[left]

    return j

def QuickSort(arr, left, right, elem) -> list:
    while left < right:
        mid = Partition(arr, left, right, elem)

        # Смотрим, какой отрезок короче для < количества рекурсий
        if mid - left < right - mid:
            QuickSort(arr, left, mid - 1, elem)
            left = mid + 1
        else:
            QuickSort(arr, mid + 1, right, elem)
            right = mid - 1

    return arr

def BinarySearch(arr, num, left, right, elem) -> int:
    mid = 0

    while left < right and arr[mid][elem] != num:
        mid = (left + right) // 2

        if arr[mid][elem] < num:
            left = mid + 1
        elif arr[mid][elem] > num:
            right = mid

    if not elem:
        while mid < len(arr) and arr[mid][0] <= num:
            mid += 1
    else:
        while mid < len(arr) and arr[mid][1] < num:
            mid += 1

    return mid

n, m = map(int, input().split())

segment = []
for i in range(n):
    a, b = map(int, input().split())
    segment.append([a, b])

points = list(map(int, input().split()))
result = [0] * len(points)

sortedLeft = QuickSort(segment.copy(), 0, len(segment) - 1, 0)
sortedRight = QuickSort(segment.copy(), 0, len(segment) - 1, 1)

for i in range(len(points)):
    result[i] += BinarySearch(sortedLeft, points[i], 0, len(segment) - 1, 0)
    result[i] -= BinarySearch(sortedRight, points[i], 0, result[i], 1)

print(*result)
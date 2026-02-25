# Input 2 lines:
#  1 line = amount elements
#  2 line = elements (list of elements)

# Output: amount of a[i] > a[j]
#                   0 ≤ i < j ≤ len(a)

def merge(left, right):
    global counter
    result = []
    indLeft = 0
    indRight = 0

    while indLeft < len(left) and indRight < len(right):
        if left[indLeft] <= right[indRight]:
            result.append(left[indLeft])
            indLeft += 1
        else:
            result.append(right[indRight])
            indRight += 1
            counter += (len(left) - indLeft)

    while indLeft < len(left):
        result.append(left[indLeft])
        indLeft += 1

    while indRight < len(right):
        result.append(right[indRight])
        indRight += 1

    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = mergeSort(arr[:mid])
    rightHalf = mergeSort(arr[mid:])

    return merge(leftHalf, rightHalf)

# 1. Input data
amount = int(input())
elemList = list(map(int, input().split()))

# 2. Initialization (global parameter)
counter = 0

# 3. Merge Sort
mergeSort(elemList)

# 4. Output data
print(counter)
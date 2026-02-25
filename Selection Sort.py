def SelectionSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i+1, length):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    import numpy as np
    arr = np.random.randint(-100, 101, 10000)
    print("Original array:", arr)
    SelectionSort(arr)
    print("Result:", arr)
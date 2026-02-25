import math


def shiftUp(currHeap, ind):
    while ind > 0 and currHeap[math.floor((ind - 1)/2)] < currHeap[ind]:
        temp = currHeap[math.floor((ind - 1)/2)]
        currHeap[math.floor((ind - 1)/2)] = currHeap[ind]
        currHeap[ind] = temp
        ind = math.floor((ind - 1)/2)

def shiftDown(currHeap, ind):
    while True:
        left = 2*ind + 1
        right = 2*ind + 2
        largest = ind

        if left < len(currHeap) and currHeap[left] > currHeap[largest]:
            largest = left

        if right < len(currHeap) and currHeap[right] > currHeap[largest]:
            largest = right

        if ind == largest:
            break

        temp = currHeap[largest]
        currHeap[largest] = currHeap[ind]
        currHeap[ind] = temp

        ind = largest

def insertNum(currHeap, priorInd):
    currHeap.append(priorInd)
    shiftUp(currHeap, len(currHeap)-1)

def extractMax(currHeap):
    temp = currHeap[0]
    currHeap[0] = currHeap[len(currHeap)-1]
    currHeap[len(currHeap)-1] = temp

    result = currHeap.pop(len(currHeap)-1)

    shiftDown(currHeap, 0)

    return result


heap = []
numOperations = int(input())

for i in range(numOperations):
    data = input().split()
    if data[0] == "Insert":
        insertNum(heap, int(data[1]))
    elif data[0] == "ExtractMax":
        print(extractMax(heap))
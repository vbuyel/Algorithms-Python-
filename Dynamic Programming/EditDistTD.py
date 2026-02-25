def EditDistTD(i, j, const, word1, word2, arr):
    if arr[i][j] == const:
        if i == 0:
            arr[i][j] = j
        elif j == 0:
            arr[i][j] = i
        else:
            insert = EditDistTD(i, j - 1, const, word1, word2, arr) + 1
            delete = EditDistTD(i - 1, j, const, word1, word2, arr) + 1
            subst = EditDistTD(i - 1, j - 1, const, word1, word2, arr) + (word1[i-1] != word2[j-1])
            arr[i][j] = min(insert, delete, subst)
    return arr[i][j]

word1 = "Hello"
word2 = "World"
arr = [[float('inf')] * (len(word2)+1) for _ in range(len(word1)+1)]
temp = EditDistTD(len(word1), len(word2), float('inf'), word1, word2, arr)
print(temp)
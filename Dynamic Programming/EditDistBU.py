def EditDistBU(word1, word2):
    matrix = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

    for i in range(len(word1) + 1):
        matrix[i][0] = i
    for j in range(len(word2) + 1):
        matrix[0][j] = j

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            const = (word1[i-1] != word2[j-1])
            matrix[i][j] = min(matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + const)

    return matrix[-1][-1]

print(EditDistBU(input(), input()))
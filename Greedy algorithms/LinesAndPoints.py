S = []
n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    S.append([x,y])

def getKey(item):
    return item[1]
S.sort(key = getKey)

i = 0
j = 1
counter = 0
resultPoints = []
while i < n:
    if j < n and S[j][0] <= S[i][1]:
        j += 1
    else:
        j -= 1
        if S[i][0] < S[j][0]:
            counter += 1
        else:
            counter += 1
        resultPoints.append(S[i][1])
        j += 1
        i = j
        j += (j < n-1)

print(counter)
for p in resultPoints:
    print(p, end=" ")
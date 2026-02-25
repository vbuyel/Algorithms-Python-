S = []
G = []
x, y = map(int, input().split())
G.append([x, y])
for i in range(G[0][0]):
    x,y = map(int, input().split())
    S.append([x,y])

def getKey(item):
    return item[0]/item[1]
S.sort(key = getKey)

cost = 0
ind = G[0][0]
while ind >= 0:
    ind -= 1
    i = 0
    if ind >= 0:
        i = S[ind][1]
    while G[0][1] > 0 and i > 0:
        G[0][1] -= 1
        i -= 1
        cost += S[ind][0]/S[ind][1]
print("{:.3f}".format(cost))
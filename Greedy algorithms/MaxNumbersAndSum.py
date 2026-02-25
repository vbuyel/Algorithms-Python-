x = int(input())

S = []
count = 0
i = 0
while x > 0:
    i += 1
    if x - i > i or x - i == 0:
        x -= i
        S.append(i)
        count += 1
print(count)
for k in range(len(S)):
    print(S[k], end=" ")
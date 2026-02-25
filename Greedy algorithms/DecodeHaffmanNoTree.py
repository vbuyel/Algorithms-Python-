# 1. *количество букв* *длина кода строки*
numChars, lengthCode = map(int, input().split())

# 2. *буква*: *код*
dataArr = []
for i in range(numChars):
    tempChar, tempCode = map(str, input().split(": "))
    dataArr.append([tempChar, tempCode])

# 3. Код строки
code = str(input())

# 4. Проход по коду -> итоговая строка
result = ""
currChar = ""
i = 0
while i < lengthCode:
    currChar += code[i]
    for j in range(numChars):
        if currChar == dataArr[j][1]:
            result += dataArr[j][0]
            currChar = ""
            break # !
    i += 1

print(result)
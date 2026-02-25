class Tree:
    def __init__(self, cargo, left = None, right = None):
        self.cargo = cargo
        self.left = left
        self.right = right

def compare(item, char):
    if isinstance (item, Tree):
        return compare(item.cargo, char)
    else:
        return item[0] == char

def compareLen(item, length):
    if isinstance (item, Tree):
        return compareLen(item.cargo, length)
    else:
        return len(item) == length

def charcode(root, char):
    # Если текущий узел - лист (строка)
    if not isinstance(root, Tree):
        return root[2] if root[0] == char else ""

    # Рекурсивно ищем в левом поддереве
    left_code = charcode(root.left, char)
    if left_code:
        return root.cargo[2] + left_code if compareLen(root, 3) else left_code

    # Рекурсивно ищем в правом поддереве
    right_code = charcode(root.right, char)
    if right_code:
        return root.cargo[2] + right_code if compareLen(root, 3) else right_code

    # Если символ не найден
    return ""

def getKey(item):
    if isinstance(item, Tree):
        return item.cargo[1]
    else:
        return item[1]

def getStr(item):
    if isinstance(item, Tree):
        return item.cargo[0]
    else:
        return item[0]

def appEnd(item, thisStr):
    if isinstance(item, Tree):
        return item.cargo.append(thisStr)
    else:
        return item.append(thisStr)
# -----

inputStr = str(input())

# Определяем частоту каждой буквы
charArr = [[inputStr[0], 0]]
for i in range(len(inputStr)):
    checkChar = False
    for j in range(len(charArr)):
        if inputStr[i] in charArr[j]:
            charArr[j][1] += 1
            checkChar = True
            break
    if not checkChar:
        charArr.append([inputStr[i], 1])

# Сортируем
charArr.sort(key = getKey)
saveCharArr = []
for i in range(len(charArr)):
    saveCharArr.append(charArr[i][0])

# Строим дерево
while len(charArr) > 1:
    left = charArr.pop(0)
    appEnd(left, "0")
    right = charArr.pop(0)
    appEnd(right, "1")
    newCargo = [getStr(left) + getStr(right), getKey(left) + getKey(right)]

    currNode = Tree(newCargo, left, right)
    charArr.append(currNode)
    charArr.sort(key=getKey)

if len(saveCharArr) == 1:
    charArr[0].append("0")

tree = charArr[0] if charArr else None

# Кодируем строку
i = 0
codeResult = ""
while i < len(inputStr):
    codeResult += charcode(tree, inputStr[i])
    i += 1

# Вывод на консоль
print(len(saveCharArr), len(codeResult))
saveCharArr.reverse()
for i in range(len(saveCharArr)):
    print(saveCharArr[i] + ": " + charcode(tree, saveCharArr[i]))

print(codeResult)
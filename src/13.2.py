def getRowsDiff(row1, row2):
    cnt = 0
    for i in range(0, len(row1)):
        if row1[i] != row2[i]:
            cnt += 1
    return cnt

def getHorizontalReflectionLineNumber(pattern):
    for i in range(0, len(pattern) - 1):
        diff = getRowsDiff(pattern[i], pattern[i + 1])
        if diff > 1:
            continue
        topIndex = i-1
        lowIndex = i+2
        isReflectionNumber = True
        while lowIndex < len(pattern) and topIndex >= 0:
            diff += getRowsDiff(pattern[lowIndex], pattern[topIndex])
            if diff > 1:
                break
            else:
                lowIndex += 1
                topIndex -= 1
        if diff == 1:
            return i + 1
    return -1

def getVerticalReflectionLineNumber(pattern):
    rotatedPattern = []
    for col in range(len(pattern[0])):
        rotatedPattern.append([])
        for row in range(len(pattern)):
            rotatedPattern[col].append(pattern[row][col])

    rotatedPattern = [''.join(line) for line in rotatedPattern]

    return getHorizontalReflectionLineNumber(rotatedPattern)

lines = open('./inputs/13.2.txt', 'r').readlines()

patterns = []
cnt = 0
while cnt < len(lines):
    curPattern = []
    while cnt < len(lines) and lines[cnt] != '\n':
        curPattern.append(lines[cnt].strip())
        cnt += 1
    patterns.append(curPattern)
    cnt += 1

rowReflections = 0
columnReflections = 0

rowReflections = 0
columnReflections = 0
for pattern in patterns:
    reflection = getHorizontalReflectionLineNumber(pattern)
    if reflection != -1:
        rowReflections += reflection
    else:
        columnReflections += getVerticalReflectionLineNumber(pattern)

print(100 * rowReflections + columnReflections)
lines = open('./inputs/10.1.txt', 'r').readlines()
lines = [line.strip() for line in lines]

n = len(lines)
m = len(lines[0])

pipes = {'|': [(1, 0), (-1, 0)], '-': [(0, 1), (0, -1)], 'L': [(-1, 0), (0, 1)],
         'J': [(-1, 0), (0, -1)], '7': [(1, 0), (0, -1)], 'F': [(1, 0), (0, 1)]}

def findSPosition(lines, n, m):
    for i in range(0, n):
        for j in range (0, m):
            if lines[i][j] == 'S':
                return (i, j)
            
def getNextStep(lines, prevStep, curStep, n, m):
    if curStep[0] < 0 or curStep[0] >= n or curStep[1] < 0 or curStep[1] >= m:
        return (-1, -1)
    
    if lines[curStep[0]][curStep[1]] == '.':
        return (-1, -1)
    
    pipe = lines[curStep[0]][curStep[1]]
    directions = pipes[pipe]
    firstPossibleStep = (curStep[0] + directions[0][0], curStep[1] + directions[0][1])
    secondPossibleStep = (curStep[0] + directions[1][0], curStep[1] + directions[1][1])

    if prevStep == firstPossibleStep:
        return secondPossibleStep
    elif prevStep == secondPossibleStep:
        return firstPossibleStep
    else:
        return (-1, -1) 
            
def getCycleLength(lines, startPos, direction, n, m):
    prevStep = startPos
    curStep = (startPos[0] + direction[0], startPos[1] + direction[1])
    steps = 1

    if curStep[0] < 0 or curStep[0] >= n or curStep[1] < 0 or curStep[1] >= m:
        return -1
    
    while lines[curStep[0]][curStep[1]] != 'S':
        nextStep = getNextStep(lines, prevStep, curStep, n, m)

        if nextStep == (-1, -1):
            return -1
        
        prevStep = curStep
        curStep = nextStep
        steps += 1

    return steps
            
sPos = findSPosition(lines, n, m)
length = -1

for direction in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
    length =  getCycleLength(lines, sPos, direction, n, m)
    if length != -1:
        break

print(length // 2)
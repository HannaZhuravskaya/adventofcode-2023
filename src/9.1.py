lines = open('./inputs/9.1.txt', 'r').readlines()

def findNextOasis(values) -> int:
    allZeroes = False
    curLength = len(values)

    while not allZeroes:
        allZeroes = True
        for i in range(0, curLength - 1):
            values[i] = values[i + 1] - values[i]

            if values[i] != 0:
                allZeroes = False 
        curLength -= 1

    for i in range(curLength, len(values)):
        values[i] = values[i-1] + values[i]

    return values[-1]

sum = 0
for line in lines:
    values = [int(x) for x in line.strip().split()]
    sum += findNextOasis(values)

print(sum)
lines = open('./inputs/9.2.txt', 'r').readlines()

def findNextOasis(values) -> int:
    allZeroes = False
    curLength = 0

    while not allZeroes:
        allZeroes = True
        for i in range(len(values)-1, curLength, -1):
            values[i] = values[i] - values[i - 1]

            if values[i] != 0:
                allZeroes = False 
        curLength += 1

    for i in range(curLength, -1, -1):
        values[i] = values[i] - values[i+1]

    return values[0]

sum = 0
for line in lines:
    values = [int(x) for x in line.strip().split()]
    sum += findNextOasis(values)

print(sum)
lines = open('./inputs/14.1.txt', 'r').readlines()
lines = [list(line.strip()) for line in lines]

rows = len(lines)
cols = len(lines[0])

def findNextFreeSpot(startIndex, lines, column):
    cur = startIndex
    while cur < len(lines) and lines[cur][column] != '.':
        cur += 1
    return cur

for i in range(0, cols):
    freeSpot = findNextFreeSpot(0, lines, i)
    for j in range(freeSpot + 1, rows):
        if freeSpot == rows:
            break
        if lines[j][i] == 'O' and freeSpot < j:
            lines[freeSpot][i] = 'O'
            lines[j][i] = '.'
            freeSpot = findNextFreeSpot(freeSpot + 1, lines, i)
        elif lines[j][i] == '#':
            freeSpot = findNextFreeSpot(j + 1, lines, i)

load = 0
for i in range(0, rows):
    for j in range(0, cols):
        if lines[i][j] == 'O':
            load += len(lines) - i
print(load)
import re

file = open('./inputs/3.1.txt', 'r')
rows = file.read().splitlines()

n = len(rows)
m = len(rows[0])

def findEndOfNumber(row, sIndex):
    eIndex = sIndex
    while eIndex < len(row) and row[eIndex].isdigit():
        eIndex += 1
    return eIndex - 1 

def isPartNumber(rows, height, start, end, n, m):
    for i in range(max(height - 1, 0), min(height + 2, n)):
        for j in range(max(start - 1, 0), min(end + 2, m)):
            element = rows[i][j]
            if element != '.' and not element.isdigit(): 
                return int(''.join(rows[height][start:end+1]))
    return 0

sum = 0

for i in range(0, n):
    j = 0
    while j < m:
        if rows[i][j].isdigit():
             endOfNumberIndex = findEndOfNumber(rows[i], j)
             sum += isPartNumber(rows, i, j, endOfNumberIndex, n, m)
             j = endOfNumberIndex
        j += 1     
 
print(sum)
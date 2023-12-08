import re

file = open('./inputs/3.2.txt', 'r')
rows = file.read().splitlines()
rows = [list(row) for row in rows]

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
            partNumber =  ''.join(rows[height][start:end+1])

            if rows[i][j] == '*':
                rows[i][j] = 'G1 ' + partNumber
            elif rows[i][j].startswith('G1'):
                rows[i][j] = 'G2' + rows[i][j] + ' ' + partNumber 
            elif rows[i][j].startswith('G2'):
                rows[i][j] = 'G3'

for i in range(0, n):
    j = 0
    while j < m:
        if rows[i][j].isdigit():
             endOfNumberIndex = findEndOfNumber(rows[i], j)
             isPartNumber(rows, i, j, endOfNumberIndex, n, m)
             j = endOfNumberIndex
        j += 1   

sum = 0

for i in range(0, n):
    for j in range(0, m):
        if rows[i][j].startswith('G2'):
            parsed = rows[i][j].split()
            sum += int(parsed[1]) * int(parsed[2])
 
print(sum)
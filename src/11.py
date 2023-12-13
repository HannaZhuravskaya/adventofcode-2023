lines = open('./inputs/11.txt', 'r').readlines()
lines = [line.strip() for line in lines]

def getShortestPathsSum(galaxies):
    sum = 0
    for i in range(0, len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            sum += abs(galaxies[i][0]-galaxies[j][0]) + abs(galaxies[i][1]-galaxies[j][1])
    return sum

def getShortestPath(lines, expander):
    galaxies = []
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])):
            if lines[i][j] == '#':
                galaxies.append((i, j))

    expandedRows = [0]
    for i in range(0, len(lines)):
        expanded = True
        for j in range(0, len(lines[i])):
            if lines[i][j] == '#':
                expanded = False
                break
        if expanded:
            expandedRows.append(expandedRows[i] + (expander - 1))
        else:
            expandedRows.append(expandedRows[i])

    expandedColumns = [0]
    for col in range(0, len(lines[0])):
        expanded = True
        for row in range(0, len(lines)):
            if lines[row][col] == '#':
                expanded = False
                break
        if expanded:
            expandedColumns.append(expandedColumns[col] + (expander - 1))
        else:
            expandedColumns.append(expandedColumns[col])

    for i in range(0, len(galaxies)):
        oldRow = galaxies[i][0]
        oldColumn =  galaxies[i][1]
        newRow = expandedRows[oldRow + 1]
        newColumn = expandedColumns[oldColumn + 1]
        galaxies[i] = (newRow + oldRow, newColumn + oldColumn)

    return getShortestPathsSum(galaxies)

            
e2 = getShortestPath(lines, 2)
e1000000 = getShortestPath(lines, 1000000)

print ('Expander 2: ', e2)
print('Expander 1000000: ',e1000000)
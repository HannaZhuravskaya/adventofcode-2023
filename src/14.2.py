lines = open('./inputs/14.2.txt', 'r').readlines()
lines = [list(line.strip()) for line in lines]

rows = len(lines)
cols = len(lines[0])

direction = {
    # direction (iterating step), iterating from, iterating to
    'north':(1, 0, rows),
    'south':(-1, rows - 1, -1), 
    'west':(1, 0, cols),
    'east':(-1, cols - 1, -1), 
}

def findNextFreeSpotV(startIndex, lines, column, dir):
    cur = startIndex
    for j in range(cur + dir[0], dir[2], dir[0]):
        if lines[cur][column] != '.':
            cur = j
        else:
            break
    return cur

def findNextFreeSpotH(startIndex, lines, row, dir):
    cur = startIndex
    for j in range(cur + dir[0], dir[2], dir[0]):
        if lines[row][cur] != '.':
            cur = j
        else:
            break
    return cur

def moveVertically(lines, rows, cols, dir):
    for i in range(0, cols):
        freeSpot = findNextFreeSpotV(dir[1], lines, i, dir)
        for j in range(freeSpot + dir[0], dir[2], dir[0]):
            if freeSpot == rows:
                break
            if lines[j][i] == 'O' and freeSpot * dir[0] < j * dir[0]:
                lines[freeSpot][i] = 'O'
                lines[j][i] = '.'
                freeSpot = findNextFreeSpotV(freeSpot + dir[0], lines, i, dir)
            elif lines[j][i] == '#':
                freeSpot = findNextFreeSpotV(j + dir[0], lines, i, dir)
    return lines

def moveHorizontally(lines, rows, cols, dir):
    for i in range(0, rows):
        freeSpot = findNextFreeSpotH(dir[1], lines, i, dir)
        for j in range(freeSpot + dir[0], dir[2], dir[0]):
            if freeSpot == cols:
                break
            if lines[i][j] == 'O' and freeSpot * dir[0] < j * dir[0]:
                lines[i][freeSpot] = 'O'
                lines[i][j] = '.'
                freeSpot = findNextFreeSpotH(freeSpot + dir[0], lines, i, dir)
            elif lines[i][j] == '#':
                freeSpot = findNextFreeSpotH(j + dir[0], lines, i, dir)
    return lines

def getAsString(arr):
    answer = ''
    for a in arr:
        answer = ''.join([answer, ''.join(a)]) 
    return answer

answers = {}
step = -1
start = 0
for i in range(0, 10000):
    lines = moveVertically(lines, rows, cols, direction['north'])
    lines = moveHorizontally(lines, rows, cols, direction['west'])
    lines = moveVertically(lines, rows, cols, direction['south'])
    lines = moveHorizontally(lines, rows, cols, direction['east'])
    key = getAsString(lines)

    if key not in answers:
        answers[key] = i
    else:
        start = answers[key]
        step = i - start
        break 
  
iteration = 1000000000
iteration = (iteration - 1 - start) % step + start
print('step: ',  step, ', start: ', start, ', real iteration: ', iteration, sep='')

lines = open('./inputs/14.2.txt', 'r').readlines()
lines = [list(line.strip()) for line in lines]

for i in range(0, iteration + 1):
    lines = moveVertically(lines, rows, cols, direction['north'])
    lines = moveHorizontally(lines, rows, cols, direction['west'])
    lines = moveVertically(lines, rows, cols, direction['south'])
    lines = moveHorizontally(lines, rows, cols, direction['east'])

load = 0
for i in range(0, rows):
    for j in range(0, cols):
        if lines[i][j] == 'O':
            load += len(lines) - i
print(load)
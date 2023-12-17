lines = open('./inputs/16.1.txt', 'r').readlines()
lines = [list(line.strip()) for line in lines]

directions = {
    '.' : {(0, 1): (0, 1), (1, 0): (1, 0), (0, -1): (0, -1), (-1, 0): (-1, 0)},
    '/' : {(0, 1): (-1, 0), (1, 0): (0, -1), (0, -1): (1, 0), (-1, 0): (0, 1)},
    '\\' : {(0, 1): (1, 0), (1, 0): (0, 1), (0, -1): (-1, 0), (-1, 0): (0, -1)},
    '-' : {(0, 1): (0, 1), (0, -1): (0, -1) },
    '|' : {(1, 0): (1, 0), (-1, 0): (-1, 0)},
}

def fingBeamPath(beam, rows, cols, field, beams, energized, visited):
    cur = beam[0]
    dir = beam[1]
    visitedInCurrentPath = set()

    while cur[0] >= 0 and cur[0] < rows and cur[1] >= 0 and cur[1] < cols and (cur, dir) not in visitedInCurrentPath:
        visitedInCurrentPath.add((cur, dir))
        energized[cur[0]][cur[1]] = '#'
        curSymbol = field[cur[0]][cur[1]]
        if dir in directions[curSymbol]:
            dir = directions[curSymbol][dir]
        elif curSymbol == '-':
            dirLeft = (0, -1)
            nextLeft = (cur[0] + dirLeft[0], cur[1] + dirLeft[1])
            if (nextLeft, dirLeft) not in visited:
                beams.append((nextLeft, dirLeft))
            dir = (0, 1)
        elif curSymbol == '|':
            dirDown = (-1, 0)
            nextDown = (cur[0] + dirDown[0], cur[1] + dirDown[1])
            if (nextDown, dirDown) not in visited:
                beams.append((nextDown, dirDown))
            dir = (1, 0)
        cur = (cur[0] + dir[0], cur[1] + dir[1])

rows = len(lines)
cols = len(lines[0])

# beams = [(startPoint, direction)]
visited = set()
beams = [((0, 0), (0, 1))]
energized = [['.' for j in range(0, cols)] for i in range(0, rows)]

while len(beams) > 0:
    beam = beams[0]
    fingBeamPath(beam, rows, cols, lines, beams, energized, visited)
    visited.add(beam)
    beams.remove(beam)

numOfEnergized = 0
for i in range(0, rows):
    for j in range(0, cols):
        if energized[i][j] == '#':
            numOfEnergized += 1
print(numOfEnergized)
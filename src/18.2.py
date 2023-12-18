import re

lines = open('./inputs/18.2.txt', 'r').readlines()
lines = [line.strip() for line in lines]

def getArea(cycle):
    #Shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula
    doubleArea = 0
    for i in range(0, len(cycle)):
        (x1, y1) = cycle[i]
        (x2, y2) = cycle[(i+1) % len(cycle)]
        doubleArea += (x1 * y2) - (x2 * y1) 
    return abs(doubleArea) / 2

def getCycleLength(cycle):
    length = 0
    for i in range(0, len(cycle)):
        (x1, y1) = cycle[i]
        (x2, y2) = cycle[(i+1) % len(cycle)]
        length += abs(x1 - x2) +  abs(y1 - y2) 
    return length

directions = {'0': (0, 1), '2': (0, -1), '3': (-1, 0), '1': (1, 0)}

points = [(0, 0)]
for i in range(0, len(lines)):
    step, dir = re.findall(r".*#([a-zA-Z=0-9\=-]+)([0-3]{1})", lines[i])[0]
    step = int(step, 16)
    point = (points[i][0] + int(step) * directions[dir][0], points[i][1] + int(step) * directions[dir][1])
    if point != (0, 0):
        points.append(point)

area = getArea(points)
length = getCycleLength(points)
#Pick's theorem: https://en.wikipedia.org/wiki/Pick%27s_theorem
numberOfInnerTiles = area - (length / 2) + 1
print(numberOfInnerTiles + length)
import re
import math

file = open('./inputs/8.2.txt', 'r')
lines = file.readlines()

instructions = lines[0].strip()

rules = {}
cur = []

for i in range(2, len(lines)):
    parsedLine = re.findall(r"([A-Z1-9]+) = \(([A-Z1-9]+), ([A-Z1-9]+)\)", lines[i])
    rules[parsedLine[0][0]] = (parsedLine[0][1], parsedLine[0][2])

    if parsedLine[0][0][2] == 'A':
        cur.append(parsedLine[0][0])

steps = []

for i in range(0, len(cur)):
    curSteps = 0

    while cur[i][2] != 'Z':
        direction = instructions[curSteps % len(instructions)]

        if direction == 'L':
            cur[i] = rules[cur[i]][0]
        else:
            cur[i] = rules[cur[i]][1]

        curSteps += 1
    steps.append(curSteps)

print(math.lcm(*steps))
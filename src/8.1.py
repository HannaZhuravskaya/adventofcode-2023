import re

file = open('./inputs/8.1.txt', 'r')
lines = file.readlines()

instructions = lines[0].strip()

rules = {}
cur = 'AAA'

for i in range(2, len(lines)):
    parsedLine = re.findall(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)", lines[i])
    rules[parsedLine[0][0]] = (parsedLine[0][1], parsedLine[0][2])

steps = 0

while cur != 'ZZZ':
    direction = instructions[steps % len(instructions)]

    if direction == 'L':
        cur = rules[cur][0]
    else:
        cur = rules[cur][1]

    steps += 1

print(steps)
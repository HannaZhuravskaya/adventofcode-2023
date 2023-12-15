import re

input = open('./inputs/15.2.txt', 'r').read().strip()
sequences = re.findall(r"([a-zA-Z=0-9\=-]+)", input)

def findHash(str):
    hash = 0
    for char in str:
        hash += ord(char)
        hash *= 17
        hash %= 256
    return hash

lengths = [[] for i in range(0, 256)]

for sequence in sequences:
    if '-' in sequence:
        label = sequence[0:-1]
        length = findHash(label)
        for i in range(0, len(lengths[length])):
            if lengths[length][i][0] == label:
                del lengths[length][i]
                break
    else:
        label, focus = sequence.split('=')
        length = findHash(label)
        index = -1
        for i in range(0, len(lengths[length])):
            if lengths[length][i][0] == label:
                index = i

        if index == -1:
            lengths[length].append((label, int(focus)))
        else:
            lengths[length][index] = (label, int(focus))

sum = 0
for i in range(0, len(lengths)):
    for j in range(0, len(lengths[i])):
        sum += (i + 1) * (j + 1) * lengths[i][j][1]
print(sum)
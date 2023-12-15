import re

input = open('./inputs/15.1.txt', 'r').read().strip()
sequences = re.findall(r"([a-zA-Z=0-9\=-]+)", input)

def findHash(str):
    hash = 0
    for char in str:
        hash += ord(char)
        hash *= 17
        hash %= 256
    return hash

sum = 0
for sequence in sequences:
    sum += findHash(sequence)

print(sum)
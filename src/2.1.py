import re

file = open('./inputs/2.1.txt', 'r')
lines = file.readlines()

cubes = {'red': 12 , 'green': 13, 'blue': 14}

sum = 0

for line in lines:
    regex = re.findall(r"Game ([0-9]+):(.+)", line)
    groupId = int(regex[0][0])
    sets = regex[0][1].split(';')
    isGoodSet = True

    for set in sets:
        subsets = set.split(',')
        for subset in subsets:
            s = subset.strip().split()
            if int(s[0]) > cubes[s[1]]:
                isGoodSet = False
                break
    
    if isGoodSet == True:
        sum += groupId
 
print(sum)
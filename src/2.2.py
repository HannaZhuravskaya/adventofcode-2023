import re

file = open('./inputs/2.2.txt', 'r')
lines = file.readlines()

sum = 0

for line in lines:
    regex = re.findall(r"Game ([0-9]+):(.+)", line)
    groupId = int(regex[0][0])
    sets = regex[0][1].split(';')

    cubes = {'red': 0 , 'green': 0, 'blue': 0}

    for set in sets:
        subsets = set.split(',')
        for subset in subsets:
            s = subset.strip().split()
            if int(s[0]) > cubes[s[1]]:
                cubes[s[1]] = int(s[0])

    power = cubes['blue'] * cubes['green'] * cubes['red']
    print(power)
    
    sum += power
 
print(sum)
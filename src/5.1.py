import re

file = open('./inputs/5.1.txt', 'r')
input = file.read()

seedsInput = re.findall(r"seeds:([0-9 ]+)", input)[0].strip().split()
seeds = [[int(seed)] for seed in seedsInput]

convertionStep = 0

mapsInput = re.findall(r"(([a-z-]+) map:([0-9\s]+))", input)
for map in mapsInput:
    mapName = map[1]
    mapRowsInput = map[2].strip().split('\n')

    dict = {}

    for mapRowInput in mapRowsInput:
       mapping = mapRowInput.strip().split()
       dest = int(mapping[0])
       src = int(mapping[1])
       diff = int(mapping[2])
       
       dict[src] = src-dest 

       if (src + diff) not in dict:
          dict[src + diff] = 0

    mappings = sorted(dict.items())

    for seed in seeds:
       cur = seed[convertionStep]
       
       if cur < mappings[0][0] or cur >= mappings[len(mappings)-1][0]:
          seed.append(cur)
       else:
          for i in range(0, len(mappings)-1):
             if mappings[i][0] <= cur and cur < mappings[i+1][0]:
                seed.append(cur - mappings[i][1])
                break

    convertionStep += 1

lowestLocation = min(seed[len(seed)-1] for seed in seeds)
print(lowestLocation)
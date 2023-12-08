import re
import sys

def getNewIntervals(seeds, translations):
    newIntervals = []

    for translation in translations:
       (tDest, tSource, tLength) = translation
       tStart = tSource
       tEnd = tSource + tLength

       newSeeds = []

       while len(seeds) > 0:
          (sStart, sEnd) = seeds.pop()

          before = (sStart, min(sEnd, tStart))
          middle = (max(sStart, tStart), min(sEnd, tEnd))
          after = (max(sStart, tEnd), sEnd)

          if before[1] > before[0]:
             newSeeds.append(before)
          if middle[1] > middle[0]:
             newIntervals.append((middle[0] - tSource + tDest, middle[1] - tSource + tDest))
          if after[1] > after[0]:
             newSeeds.append(after)
       
       seeds = newSeeds 
    return newIntervals + seeds

file = open('./inputs/5.2.txt', 'r')
input = file.read()

seedsInput = re.findall(r"seeds:([0-9 ]+)", input)[0].strip().split()
seedsInput = [int(seed) for seed in seedsInput]

seeds = []
for i in range(0, len(seedsInput) - 1, 2):
   seeds.append((seedsInput[i], seedsInput[i] + seedsInput[i+1]))

maps = []

mapsInput = re.findall(r"(([a-z-]+) map:([0-9\s]+))", input)
for map in mapsInput:
    mapRowsInput = map[2].strip().split('\n')

    mappings = []

    for mapRowInput in mapRowsInput:
       mapping = [int(x) for x in mapRowInput.strip().split()]
       mappings.append((int(mapping[0]), int(mapping[1]), int(mapping[2])))

    maps.append(mappings)

mins = []

for seed in seeds:
  splittedSeeds = [seed]
  for map in maps:
    splittedSeeds = getNewIntervals(splittedSeeds, map)
  mins.append(min(splittedSeeds)[0])

print(min(mins))
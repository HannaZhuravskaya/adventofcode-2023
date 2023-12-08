import re
import sys

def getNewIntervals(seeds, translations):
    newIntervals = []

    sIndex = 0
    tIndex = 0

    while sIndex < len(seeds) and tIndex < len(translations):
      sLeft = seeds[sIndex][0]
      sRight = seeds[sIndex][1]
      sDiff = seeds[sIndex][2]
      tLeft = translations[tIndex][0]
      tRight = translations[tIndex][1]
      tDiff = translations[tIndex][2]
      if sLeft < tLeft:
         if sRight < tLeft:
            print(1)
            newIntervals.append((sLeft, sRight, sDiff))
            sIndex += 1
         elif sRight ==  tLeft:
            print(2)
            newIntervals.append((sLeft, tLeft - 1, sDiff))
            newIntervals.append((tLeft, tLeft, tDiff))
            sIndex += 1
         else:
            if sRight < tRight:
               print(3)
               newIntervals.append((sLeft, tLeft - 1, sDiff))
               newIntervals.append((tLeft, sRight, tDiff))
               sIndex += 1
            elif sRight == tRight:
               print(4)
               newIntervals.append((sLeft, tLeft - 1, sDiff))
               newIntervals.append((tLeft, sRight, tDiff))
               sIndex += 1
               tIndex += 1
            else: 
               newIntervals.append((sLeft, tLeft - 1, sDiff))
               newIntervals.append((tLeft, tRight, tDiff))
               seeds[sIndex] = (tRight + 1, sRight, sDiff)
               tIndex += 1
               print(5)
            
      elif sLeft == tLeft:
         if sRight < tRight:
            newIntervals.append((tLeft, sRight, tDiff))
            sIndex += 1
            print(6)
         elif sRight == tRight:
            newIntervals.append((tLeft, sRight, tDiff))
            sIndex += 1
            tIndex += 1
            print(7)
         else:
            newIntervals.append((tLeft, tRight, tDiff))
            seeds[sIndex] = (tRight + 1, sRight, sDiff)
            tIndex += 1
            print(8)
      else:
         if sRight < tRight:
            print(9)
            newIntervals.append((sLeft, sRight, tDiff))
            sIndex += 1
         elif sRight == tRight:
            newIntervals.append((sLeft, sRight, tDiff))
            sIndex += 1
            tIndex += 1
            print(10)
         elif sLeft > tRight:
            tIndex += 1
         else:
            newIntervals.append((sLeft, tRight, tDiff))
            seeds[sIndex] = (tRight + 1, sRight, sDiff)
            tIndex += 1
            print(11)

    while sIndex < len(seeds):
       sLeft = seeds[sIndex][0]
       sRight = seeds[sIndex][1]
       sDiff = seeds[sIndex][2]
       newIntervals.append((sLeft, sRight, sDiff))
       sIndex += 1
       
    return newIntervals

def normalizeNewIntervals(intervals):
   for i in range(0, len(intervals)):
      diff = intervals[i][2]
      intervals[i] = (intervals[i][0] + diff, intervals[i][1] + diff, 0)
    
   sortedValues = sorted(intervals, key=lambda i: i[0])
   print(sortedValues)

   return sortedValues
   
print('expected : 1 : ', getNewIntervals([(0, 1, 0)], [(2, 6, -10)]))
print('expected : 2 : ', getNewIntervals([(0, 2, 0)], [(2, 6, -10)]))
print('expected : 3 : ', getNewIntervals([(0, 4, 0)], [(2, 6, -10)]))
print('expected : 4 : ', getNewIntervals([(0, 6, 0)], [(2, 6, -10)]))
print('expected : 5 : ', getNewIntervals([(0, 8, 0)], [(2, 6, -10)]))
print('expected : 6 : ', getNewIntervals([(2, 3, 0)], [(2, 6, -10)]))
print('expected : 7 : ', getNewIntervals([(2, 6, 0)], [(2, 6, -10)]))
print('expected : 8 : ', getNewIntervals([(2, 8, 0)], [(2, 6, -10)]))
print('expected : 9 : ', getNewIntervals([(3, 4, 0)], [(2, 6, -10)]))
print('expected : 10 : ', getNewIntervals([(3, 6, 0)], [(2, 6, -10)]))
print('expected : 11 : ', getNewIntervals([(3, 8, 0)], [(2, 6, -10)]))

normalizeNewIntervals([(2, 6, 10), (7, 8, 0)])

file = open('./inputs/5.2.txt', 'r')
input = file.read()

seedsInput = re.findall(r"seeds:([0-9 ]+)", input)[0].strip().split()
seedsInput = [int(seed) for seed in seedsInput]
print(seedsInput)

seeds = []

for i in range(0, len(seedsInput) - 1, 2):
   seeds.append((seedsInput[i], seedsInput[i] + seedsInput[i+1] - 1, 0))

seeds = sorted(seeds, key=lambda i: i[0])

print('seeds:', seeds)


maps = []

convertionStep = 0

mapsInput = re.findall(r"(([a-z-]+) map:([0-9\s]+))", input)
for map in mapsInput:
    mapName = map[1]
    mapRowsInput = map[2].strip().split('\n')

    mappings = []

    for mapRowInput in mapRowsInput:
       mapping = mapRowInput.strip().split()
       dest = int(mapping[0])
       src = int(mapping[1])
       diff = int(mapping[2])

       convertion = dest - src

       mappings.append((src + convertion, src + diff - 1 + convertion, -convertion))

    mappings = sorted(mappings, key=lambda i: i[0])

    print(mappings)

    maps.append((mapName, mappings))

    mappings = getNewIntervals(seeds, mappings)

    print('intersections: ', mappings)

    seeds = normalizeNewIntervals(mappings)

    print('intersections normalized: ', seeds)
   

    convertionStep += 1



        
        # 
        # print(dict)



# lowestLocation = min(seed[len(seed)-1] for seed in seeds)
# print(lowestLocation)
   


#create dict, for each row  add if defaul to protect ovverride
#  (sources, source-dest),  (source + diff, 0)
#sort
# check if less than first value - 0, bigger than lat -> 0, for each value go throug array find left <= x < right -> map to left [1]  

seedsMap = []
maps = []
#dict {'seeds-to-...',[array]} 

#for each after seeds
#create dict, for each row  add if defaul to protect ovverride
#  (sources, source-dest),  (source + diff, 0)
#sort
# check if less than first value - 0, bigger than lat -> 0, for each value go throug array find left <= x < right -> map to left [1] 


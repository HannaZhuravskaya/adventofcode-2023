import re 

file = open('./inputs/6.1.txt', 'r')
input = file.read()

regex = re.findall(r"Time:([0-9 ]*)\s*Distance:([0-9 ]*)", input)

times = regex[0][0].strip().split()
times = [int(x) for x in times]
distancies = regex[0][1].strip().split()
distancies = [int(x) for x in distancies]

def getNumOfWins(time, distance):
    wins = 0
    for i in range(1, time+1):
        if i * (time - i) > distance:
            wins +=1 
    return wins


answer = 1
for i in range (0, len(times)):
    answer *= getNumOfWins(times[i], distancies[i])


print(answer)
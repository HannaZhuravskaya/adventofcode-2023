import re 

file = open('./inputs/6.2.txt', 'r')
input = file.read()

regex = re.findall(r"Time:([0-9 ]*)\s*Distance:([0-9 ]*)", input)

time = int(regex[0][0].replace(' ', ''))
distance = int(regex[0][1].replace(' ', ''))

def getNumOfWins(time, distance):
    wins = 0
    for i in range(1, time+1):
        if i * (time - i) > distance:
            wins +=1 
    return wins


print(getNumOfWins(time, distance))